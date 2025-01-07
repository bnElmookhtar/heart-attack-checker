from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load('models/manual_model.pkl')

@app.route('/')
def home():
    """
    The home page of the application that displays the prediction form.
    """
    return render_template('predict.html')  
    return render_template('predict.html') 
@app.route('/predict', methods=['POST'])
def predict():
    """Predict if a patient has a heart disease based on input features."""
    data = request.get_json()

    input_features = np.array([
        [
            int(data['chest_pain']),
            int(data['slope']),
            int(data['thalach']),
            int(data['resting_ecg']),
            int(data['num_major_vessels']),
            int(data['age']),
            int(data['exercise_induced_angina']),
        ]
    ])
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
