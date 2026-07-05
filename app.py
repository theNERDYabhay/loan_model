import os
import sqlite3
import joblib
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "loan_prediction_project_2026"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "loan_history.db")
MODEL = joblib.load(os.path.join(BASE_DIR, "model", "loan_model.pkl"))

def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
    CREATE TABLE IF NOT EXISTS loan_history(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        age INTEGER,
        income REAL,
        loan_amount REAL,
        credit_score INTEGER,
        prediction TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    conn.commit()
    conn.close()

init_db()

@app.route("/")
def home():
    return render_template(
        "index.html",
        prediction=session.pop("prediction", None),
        age=session.pop("age", ""),
        income=session.pop("income", ""),
        loan=session.pop("loan", ""),
        credit=session.pop("credit", "")
    )

@app.route("/predict", methods=["POST"])
def predict():
    age = int(request.form["age"])
    income = float(request.form["income"])
    loan = float(request.form["loan"])
    credit = int(request.form["credit"])

    pred = MODEL.predict([[age, income, loan, credit]])[0]
    result = "Approved" if pred == 1 else "Rejected"

    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        "INSERT INTO loan_history(age,income,loan_amount,credit_score,prediction) VALUES(?,?,?,?,?)",
        (age, income, loan, credit, result)
    )
    conn.commit()
    conn.close()

    session["prediction"] = result
    session["age"] = age
    session["income"] = income
    session["loan"] = loan
    session["credit"] = credit

    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
