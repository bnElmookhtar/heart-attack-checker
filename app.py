from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)

<<<<<<< HEAD
=======
# تحميل النموذج المحفوظ
>>>>>>> f2e5a36323dc2de1b3a03a5b667fb96503c64bc3
model = joblib.load('models/manual_model.pkl')

@app.route('/')
def home():
    return render_template('predict.html') 

/*************  ✨ Codeium Command 🌟  *************/
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
/******  d2f0f486-a159-4d25-a0e3-8cb22afe3cfd  *******/

if __name__ == '__main__':
    app.run(debug=True)
