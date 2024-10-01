import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from flask import Flask, render_template, request
from const import (
    APP_HOST,
    APP_DEBUG_MODE,
    APP_PORT,
    APP_TEMPLATE_FOLDER,
    APP_STATIC_FOLDER,
    APP_STATIC_URL_PATH,
    HEART_DISEASE_COLUMNS,
    SELECTED_FEATURES,
)

app = Flask(
    __name__,
    template_folder=APP_TEMPLATE_FOLDER,
    static_folder=APP_STATIC_FOLDER,
    static_url_path=APP_STATIC_URL_PATH,
)

csv_file = "static/data/heart.csv"
heart_disease_data = pd.read_csv(csv_file)

X = heart_disease_data[SELECTED_FEATURES]
y = heart_disease_data['target']

# Train the model
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)


@app.route("/", methods=["GET", "POST"])
def index():
    result_predict = None  # Default result is None (no prediction yet)

    if request.method == "POST":
        # Retrieve user input from the form into a dictionary
        print("post")
        user_input = {
            'age': float(request.form['age']),
            'sex': float(request.form['sex']),
            'cp': float(request.form['cp']),
            'trestbps': float(request.form['trestbps']),
            'chol': float(request.form['chol']),
            'fbs': float(request.form['fbs']),
            'restecg': float(request.form['restecg']),
            'thalach': float(request.form['thalach']),
            'exang': float(request.form['exang']),
            'oldpeak': float(request.form['oldpeak']),
            'slope': float(request.form['slope']),
            'ca': float(request.form['ca']),
            'thal': float(request.form['thal'])
        }
        # Convert user input into a 2D array for prediction
        user_input_array = np.array(list(user_input.values())).reshape(1, -1)
        
        # Make a prediction using the trained model
        prediction = model.predict(user_input_array)
        
        # Map prediction result to the human-readable output
        result_predict = "มีโรคหัวใจ" if prediction[0] == 1 else "ไม่มีโรคหัวใจ"

    page = request.args.get("page", 1, type=int)
    per_page = 25
    total_rows = heart_disease_data.shape[0]
    total_pages = (total_rows + per_page - 1) // per_page

    start_row = (page - 1) * per_page
    end_row = start_row + per_page
    data_paginated = heart_disease_data.iloc[start_row:end_row]

    return render_template(
        "index.html",
        data=data_paginated.to_dict(orient="records"),
        HEART_DISEASE_COLUMNS=HEART_DISEASE_COLUMNS,
        page=page,
        total_pages=total_pages,
        result_predict=result_predict
    )


if __name__ == "__main__":
    app.run(host=APP_HOST, debug=APP_DEBUG_MODE, port=APP_PORT)
