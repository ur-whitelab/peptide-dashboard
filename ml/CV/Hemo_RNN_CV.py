#@title Runtime
use_tpu = False #@param

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import os
import tensorflow as tf
import urllib
from dataclasses import dataclass
import tensorflowjs as tfjs
import json
from sklearn.model_selection import KFold
np.random.seed(0)

print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))

urllib.request.urlretrieve(
    "https://github.com/ur-whitelab/peptide-dashboard/raw/master/ml/data/hemo-positive.npz",
    "positive.npz",
)
urllib.request.urlretrieve(
    "https://github.com/ur-whitelab/peptide-dashboard/raw/master/ml/data/hemo-negative.npz",
    "negative.npz",
)
with np.load("positive.npz") as r:
    pos_data = r[list(r.keys())[0]]
with np.load("negative.npz") as r:
    neg_data = r[list(r.keys())[0]]

# create labels and stich it all into one
# tensor
labels = np.concatenate(
    (
        np.ones((pos_data.shape[0], 1), dtype=pos_data.dtype),
        np.zeros((neg_data.shape[0], 1), dtype=pos_data.dtype),
    ),
    axis=0,
)

features = np.concatenate((pos_data, neg_data), axis=0)

print('Positive data', pos_data.shape[0])
print('Negative data', neg_data.shape[0])


@dataclass
class Config:
    vocab_size: int
    example_number: int
    batch_size: int
    buffer_size: int
    rnn_units: int
    hidden_dim: int
    embedding_dim: int
    reg_strength: float
    lr: float
    drop_rate: float
        
config = Config(vocab_size=21, # include gap
                example_number=len(labels), 
                batch_size=16, 
                buffer_size=10000,
                rnn_units=64,
                hidden_dim=64,
                embedding_dim=32,
                reg_strength=0,
                lr=1e-3,
                drop_rate=0.1
               )


def counts_aa(vec):
    counts =  tf.histogram_fixed_width(vec, [0, 20], nbins=21)[1:]
    return counts/tf.reduce_sum(counts)


describtion  = 'baseline_counts_fr_removed_first_and_second_dens_group'

def build_model(L):
    inputs = tf.keras.Input(shape=(L,))
    input_f = tf.keras.Input(shape=(20,))
    # make embedding and indicate that 0 should be treated as padding mask
    e = tf.keras.layers.Embedding(input_dim=config.vocab_size, 
                                        output_dim=config.embedding_dim,
                                        mask_zero=True)(inputs)

    # RNN layer
    x = tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(config.rnn_units, return_sequences=True))(e)
    x = tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(config.rnn_units))(x)
    x = tf.keras.layers.Concatenate()([x, input_f])
    x = tf.keras.layers.LayerNormalization()(x)
    x = tf.keras.layers.Dropout(config.drop_rate)(x)
    # a dense hidden layer
#     x = tf.keras.layers.Dense(
#         config.hidden_dim, 
#         activation='relu', 
#         kernel_regularizer=tf.keras.regularizers.l2(config.reg_strength))(x)
#     x = tf.keras.layers.Concatenate()([x, input_f])
#     x = tf.keras.layers.LayerNormalization()(x)
#     x = tf.keras.layers.Dropout(config.drop_rate)(x)
#     x = tf.keras.layers.Dense(
#         config.hidden_dim // 4, 
#         activation='relu', 
#         kernel_regularizer=tf.keras.regularizers.l2(config.reg_strength))(x)
#     x = tf.keras.layers.Concatenate()([x, input_f])
#     x = tf.keras.layers.LayerNormalization()(x)
#     x = tf.keras.layers.Dropout(config.drop_rate)(x)
    # predicting prob, so no activation
    yhat = tf.keras.layers.Dense(1, activation='sigmoid')(x) # 

    model = tf.keras.Model(inputs=[inputs, input_f], outputs=yhat, name='hemo-rnn')
    return model

if use_tpu:
  tf.keras.backend.clear_session()

  resolver = tf.distribute.cluster_resolver.TPUClusterResolver('grpc://' + os.environ['COLAB_TPU_ADDR'])
  tf.config.experimental_connect_to_cluster(resolver)

  # This is the TPU initialization code that has to be at the beginning.
  tf.tpu.experimental.initialize_tpu_system(resolver)
  print("All devices: ", tf.config.list_logical_devices('TPU'))

  strategy = tf.distribute.experimental.TPUStrategy(resolver)

i = np.arange(len(labels))
np.random.shuffle(i)
shuffled_labels = labels[i]
shuffled_features = features[i]
 
L = None#features[0].shape[-1]
N = len(shuffled_labels)

from sklearn.model_selection import ShuffleSplit
kf = KFold(n_splits=5, shuffle=True)
folds_results = []
for i, (train_index, test_index) in enumerate(kf.split(shuffled_features, shuffled_labels)):
    print(f'Running model on fold {i+1}')
    train_data = tf.data.Dataset.from_tensor_slices((shuffled_features[train_index], shuffled_labels[train_index])).map(lambda x,y: ((x, counts_aa(x)), y)).shuffle(config.buffer_size).batch(config.batch_size) 
    shuffled_features_test = shuffled_features[test_index]
    shuffled_labels_test = shuffled_labels[test_index]
    # getting indices for a 10% split of test and validation using ShuffleSplit
    sss = ShuffleSplit(n_splits=1, test_size=0.1)
    sss.get_n_splits(shuffled_features_test, shuffled_labels_test)
    val_index, test_index = next(sss.split(shuffled_features_test, shuffled_labels_test))
    val_data = tf.data.Dataset.from_tensor_slices((shuffled_features_test[val_index], shuffled_labels_test[val_index])).map(lambda x,y: ((x, counts_aa(x)), y)).shuffle(config.buffer_size).batch(config.batch_size)
    test_data = tf.data.Dataset.from_tensor_slices((shuffled_features_test[test_index], shuffled_labels_test[test_index])).map(lambda x,y: ((x, counts_aa(x)), y)).shuffle(config.buffer_size).batch(config.batch_size).prefetch(tf.data.experimental.AUTOTUNE) 
    tf.keras.backend.clear_session()
    if use_tpu:
      with strategy.scope():
        model = build_model(L)
    else:
      model = build_model(L)

      decay_epochs = 50
      decay_steps = N  // config.batch_size * decay_epochs
      lr_decayed_fn = tf.keras.optimizers.schedules.CosineDecay(
          config.lr, decay_steps, alpha=1e-3)
      opt = tf.optimizers.Adam(lr_decayed_fn)
      model.compile(
          opt,
          loss=tf.keras.losses.BinaryCrossentropy(from_logits=False),
          steps_per_execution = 60 if use_tpu else None,
          metrics=[tf.keras.metrics.AUC(from_logits=False), tf.keras.metrics.BinaryAccuracy(threshold=0.5)])
    result = model.fit(
    train_data, 
    validation_data=val_data, 
    callbacks=[tf.keras.callbacks.LambdaCallback(
        on_epoch_begin=lambda epochs,logs: print('lr =',lr_decayed_fn(opt.iterations).numpy())
        ),
        tf.keras.callbacks.EarlyStopping(monitor='val_auc', mode='max', restore_best_weights=True, patience=10)],
    epochs=150,
    verbose=0)
    test_result = model.evaluate(test_data)
    print(f'Fold {i+1}: Test AUC: {test_result[1]:.3f}  Test Accuracy: {test_result[2]:.3f}')
    folds_results.append(test_result[1:])

folds_results = np.array(folds_results)
means = np.mean(folds_results, axis=0)
stds = np.std(folds_results, axis=0)

txt = f'{describtion}\n\nMean 5-fold:\n AUC: {means[0]:.3f}   error: {stds[0]:.3f}\n ACC: {means[1]:.3f}   error: {stds[1]:.3f}'

with open(f'CV_results/{describtion}.txt', 'w') as f:
    f.write(txt)
