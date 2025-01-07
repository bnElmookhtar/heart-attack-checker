from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)

# تحميل النموذج المحفوظ
model = joblib.load('models/manual_model.pkl')

# الصفحة الرئيسية لعرض نموذج الـ HTML
@app.route('/')
def home():
    return render_template('predict.html')  # استخدام ملف predict.html من مجلد templates

# دالة لاستقبال المدخلات والتنبؤ
@app.route('/predict', methods=['POST'])
def predict():
    # استلام المدخلات من الـ HTML
    data = request.get_json()

    # استخراج المدخلات (حولها إلى نوع بيانات مناسب)
    cp = int(data['cp'])
    slope = int(data['slope'])
    thalach = int(data['thalach'])
    restecg = int(data['restecg'])
    ca = int(data['ca'])
    age = int(data['age'])
    exang = int(data['exang'])

    # تحويل المدخلات إلى مصفوفة يمكن استخدامها من قبل النموذج
    input_features = np.array([[cp, slope, thalach, restecg, ca, age, exang]])

    # إجراء التنبؤ باستخدام النموذج
    prediction = model.predict(input_features)

    # إرجاع التنبؤ كنتيجة (1 أو 0)
    return jsonify({'prediction': str(prediction[0])})

# تشغيل السيرفر
if __name__ == '__main__':
    app.run(debug=True)
