from . import lib
from quart import Quart, jsonify, request
from peptideqspr.evaluation.evaluate_peptide import Model


app = Quart(__name__)
model = None

def get_model():
    global model
    if model is None:
        model = Model()
    return model

@app.route('/predict/<query>')
def predict(query):
    prediction = get_model().predict(query)
    response = jsonify({'prediction': prediction})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
'''
@app.route('/train/start')
def train_start():
    get_model().train_start()
    return train_status()
@app.route('/train/status')
def train_status():
    status = get_model().train_status()
    response = jsonify({'status': status})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/train/stop')
async def train_stop():
    await get_model().train_stop()
    return train_status()

@app.route('/train/delete')
async def train_delete():
    await get_model().reset_model()
    response = jsonify({})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
'''
def start():
    app.run(host="0.0.0.0", debug=True, port=5000)

