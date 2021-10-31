import * as tf from '@tensorflow/tfjs';

const stoi = { "A": 0, "R": 1, "N": 2, "D": 3, "C": 4, "Q": 5, "E": 6, "G": 7, "H": 8, "I": 9, "L": 10, "K": 11, "M": 12, "F": 13, "P": 14, "S": 15, "T": 16, "W": 17, "Y": 18, "V": 19 };
const vocab = ['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V'];

const rnn_mod = {
    startLoad: (fxn) => {
        const loader = tf.loadLayersModel('https://raw.githubusercontent.com/whitead/molecule-dream/main/static/model/model.json');
        loader.then((model) => {
            rnn_mod.model = (t) => {
                return model.predict(t);
            }
            rnn_mod.model_loaded = 'loaded';
            fxn('loaded')
            rnn_mod.resetStates = () => {
                model.resetStates();
            }
        }, () => {
            rnn_mod.model_loaded = 'failed';
            fxn('failed');
        });
    }
};



rnn_mod.resetStates = () => {
    // placeholder, overwritten on load
}

rnn_mod.sample = (x, seed, T = 0.5, k = 1) => {
    return tf.multinomial(
        tf.mul(tf.scalar(1 / (T + 0.00001)), x), k, seed
    );
}

rnn_mod.seq2vec = (s) => {
    const vec = tf.tensor(Array.from(s).map((e, i) => {
        if (e)
            parseInt(stoi[e]);
    }));
    return vec;
}

rnn_mod.initVec = () => {
    return tf.tensor([0]);
}

rnn_mod.vec2seq = (v) => {
    const out = v.array().then((x) => {
        if (Array.isArray(x)) {
            return x.map((e, i) => {
                return vocab[parseInt(e)];
            });
        } else {
            return [vocab[parseInt(x)]];
        }
    });

    return out;
}

export default rnn_mod;
