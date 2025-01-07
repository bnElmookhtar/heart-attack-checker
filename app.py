from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load('models/manual_model.pkl')

@app.route('/')
def home():
    return render_template('predict.html') 

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    cp = int(data['cp'])
    slope = int(data['slope'])
    thalach = int(data['thalach'])
    restecg = int(data['restecg'])
    ca = int(data['ca'])
    age = int(data['age'])
    exang = int(data['exang'])

    input_features = np.array([[cp, slope, thalach, restecg, ca, age, exang]])

    prediction = model.predict(input_features)

    return jsonify({'prediction': str(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)
