import pickle

from flask import Flask
from flask import request
from flask import jsonify

import requests

print('start')
model_file = 'model1.bin'
dv_file= 'dv.bin'
with open(model_file, 'rb') as f_in:
    model = pickle.load(f_in)
with open(dv_file, 'rb') as f_in:
    dv = pickle.load(f_in)
print('start')
app = Flask('task_4') # give an identity to your web service

@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()

    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0, 1]
    churn = y_pred >= 0.5

    result = {
        'churn_probability': float(y_pred),
        'churn': bool(churn)
    }

    return jsonify(result)

app.run(debug=True, host='localhost', port=9696)

url = 'http://localhost:9696/predict'
client = {"job": "unknown", "duration": 270, "poutcome": "failure"}
response = requests.post(url, json=client).json()

print(response)

print('end')