
from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("model/loan_model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    age = int(request.form["age"])
    income = float(request.form["income"])
    loan_amount = float(request.form["loan"])
    credit_score = int(request.form["credit"])

    prediction = model.predict([[age, income, loan_amount, credit_score]])

    if prediction[0] == 1:
        result = "Congratulations! Your loan application has been approved."
    else:
        result = "Sorry,Loan Rejected"

    return render_template("index.html", prediction=result)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)