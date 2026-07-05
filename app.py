import os
from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Use an absolute path so the model loads correctly no matter
# which directory you run this script from
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model", "loan_model.pkl")

model = joblib.load(MODEL_PATH)

@app.route("/test")
def test():
    return "Hello World"

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        age = int(request.form["age"])
        income = float(request.form["income"])
        loan_amount = float(request.form["loan"])
        credit_score = int(request.form["credit"])

        prediction = model.predict([[age, income, loan_amount, credit_score]])

        if prediction[0] == 1:
            result = "Congratulations! Your loan application has been approved."
        else:
            result = "Sorry, Loan Rejected."

    except (KeyError, ValueError) as e:
        result = f"Invalid input: please fill in all fields with valid numbers. ({e})"

    return render_template("index.html", prediction=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)