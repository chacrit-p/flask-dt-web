import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from flask import Flask, render_template, request
from config import (
    APP_HOST,
    APP_DEBUG_MODE,
    APP_PORT,
    APP_TEMPLATE_FOLDER,
    APP_STATIC_FOLDER,
    APP_STATIC_URL_PATH,
)

app = Flask(
    __name__,
    template_folder=APP_TEMPLATE_FOLDER,
    static_folder=APP_STATIC_FOLDER,
    static_url_path=APP_STATIC_URL_PATH,
)

CSV_FILE = "static/data/heart.csv"
HEART_DISEASE_DATA = pd.read_csv(CSV_FILE)

HEART_DISEASE_COLUMNS = {
    "age": "อายุ",
    "sex": "เพศ (1 = ชาย; 0 = หญิง)",
    "cp": "ประเภทอาการเจ็บหน้าอก",
    "trestbps": "ค่าความดันโลหิต",
    "chol": "คอเลสเตอรอลในเลือด (mg/dl)",
    "fbs": "น้ำตาลในเลือดขณะอดอาหาร > 120 มก./ดล. (1 = จริง; 0 = เท็จ)",
    "restecg": "ผลการตรวจคลื่นไฟฟ้าหัวใจขณะพัก",
    "thalach": "อัตราการเต้นของหัวใจสูงสุดที่ได้รับ",
    "exang": "การออกกำลังกายทำให้เกิดโรคหลอดเลือดหัวใจตีบ (1 = ใช่; 0 = ไม่ใช่)",
    "oldpeak": "ภาวะซึมเศร้าเกิดจากการออกกำลังกายสัมพันธ์กับการพักผ่อน",
    "slope": "ความชันของส่วน ST ของการออกกำลังกายสูงสุด",
    "ca": "จำนวนหลอดเลือดที่ตีบ (0-4)",
    "thal": "สถานะของ thalassemia (1 = ปกติ; 2 = ค่าต่ำ; 3 = ค่าปานกลาง; 4 = ค่าต่ำมาก)",
    "target": "สถานะการเกิดโรคหัวใจ (1 = มีโรคหัวใจ; 0 = ไม่มีโรคหัวใจ)",
}

SELECTED_FEATURES = [
    "age",
    "sex",
    "cp",
    "trestbps",
    "chol",
    "fbs",
    "restecg",
    "thalach",
    "exang",
    "oldpeak",
    "slope",
    "ca",
    "thal",
]


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/table", methods=["GET"])
def table():
    heart_disease_table = HEART_DISEASE_DATA.head(50).to_dict(orient="records")
    return render_template(
        "table.html",
        heart_disease_table=heart_disease_table,
        HEART_DISEASE_COLUMNS=HEART_DISEASE_COLUMNS,
    )


@app.route("/predict", methods=["GET"])
def predict():
    return render_template("predict.html")


@app.route("/predict/result", methods=["POST"])
def predict_result():
    result_predict = None

    # Prepare features and target
    X = HEART_DISEASE_DATA[SELECTED_FEATURES]
    y = HEART_DISEASE_DATA["target"]

    # Split data into train and test
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Initialize and train the model
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)

    # Get the user's input from the form
    user_input = {
        "age": float(request.form["age"]),
        "sex": float(request.form["sex"]),
        "cp": float(request.form["cp"]),
        "trestbps": float(request.form["trestbps"]),
        "chol": float(request.form["chol"]),
        "fbs": float(request.form["fbs"]),
        "restecg": float(request.form["restecg"]),
        "thalach": float(request.form["thalach"]),
        "exang": float(request.form["exang"]),
        "oldpeak": float(request.form["oldpeak"]),
        "slope": float(request.form["slope"]),
        "ca": float(request.form["ca"]),
        "thal": float(request.form["thal"]),
    }

    # Convert the user's input (dictionary values) into a NumPy array
    # Reshape the array to have 1 row and as many columns as there are features (-1 lets NumPy infer the number of columns)
    user_input_array = np.array(list(user_input.values())).reshape(1, -1)

    # Use the trained model to predict whether the input indicates heart disease (1) or not (0)
    prediction = model.predict(user_input_array)

    # Assign the result message based on the prediction:
    # If the prediction is 1, it means heart disease is present, otherwise it's not
    result_predict = "มีโรคหัวใจ" if prediction[0] == 1 else "ไม่มีโรคหัวใจ"

    return render_template("predict_result.html", result_predict=result_predict)


if __name__ == "__main__":
    app.run(host=APP_HOST, debug=APP_DEBUG_MODE, port=APP_PORT)
