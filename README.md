# Heart Attack Checker

### Overview
The **Heart Attack Checker** is a web application designed to predict the likelihood of a heart attack based on several health-related inputs. The project utilizes machine learning algorithms to assess a patient's risk based on features such as chest pain type, maximum heart rate, age, and more. The application provides real-time predictions and displays relevant images based on the result.

### Features
- **Real-time Predictions**: Enter health-related data and get a prediction about the likelihood of a heart attack.
- **Interactive UI**: A user-friendly interface to input various health parameters.
- **Visual Feedback**: Displays relevant images based on the prediction outcome (healthy or at risk).
- **Responsive Design**: The application is fully responsive and adjusts seamlessly across different devices.

### Tech Stack
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python (Flask)
- **Machine Learning**: Scikit-learn

### Installation

#### Prerequisites
Make sure you have the following libraries installed via `requirements.txt`:

- Flask
- Scikit-learn
- Pandas
- Numpy
- Other dependencies as specified in `requirements.txt`.

To install them, run:
```bash
pip install -r requirements.txt
```
````
heart-attack-checker/
│
├── app.py                        # Main Python file that runs the Flask app
├── requirements.txt              # List of dependencies for the project
├── templates/                    # Folder containing HTML templates
│   └── predict.html              # Main HTML file for user input and result display
├── notebooks/                    # Jupyter Notebooks for model analysis
│   └── heart_attack_checker_manual_feature_selection.ipynb # Feature selection notebook and extracted model
├── dataset/                      # Folder containing the dataset
│   └── heart.csv                 # Dataset for training the machine learning model
├── models/                       # Folder containing trained machine learning models
│   └── manual_model.pkl          # Trained machine learning model
└── README.md                     # Project README file
````

### Machine Learning Model
The machine learning model used in this project is built using scikit-learn. The model predicts the likelihood of a heart attack based on the following features:

Chest Pain Type (cp)
Maximum Heart Rate (thalach)
Age (age)
Slope (slope)
Resting Electrocardiographic Results (restecg)
Number of Major Vessels (ca)
Exercise Induced Angina (exang)
Model Workflow
The user inputs the required data through the web interface.
The data is sent to the backend, where it is processed.
A prediction is made based on the trained machine learning model.
The prediction is displayed along with an appropriate image (indicating heart attack risk or not).

### Usage
  Enter the health parameters into the form on the main page (predict.html).
  Click the Predict button to submit the data.
  The result will appear with an image indicating the prediction:
  Heart Disease: If the prediction indicates a risk of heart attack.
  No Heart Disease: If the prediction is negative (no risk of heart attack).
