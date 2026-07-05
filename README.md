


# 🏦 Loan Approval Prediction System

A Machine Learning web application that predicts whether a customer's loan application will be **Approved** or **Rejected** based on financial and personal details.

The project demonstrates the complete Machine Learning workflow—from data preprocessing to model training, evaluation, saving the model, and deploying it using Flask.

---

#  Features

- Predict Loan Approval in real-time
- User-friendly Bootstrap Interface
- Decision Tree Machine Learning Model
- Data Preprocessing
- Model Serialization using Joblib
- Flask Backend
- Easy to deploy

---

#  Demo

Enter the following information:

- Age
- Applicant Income
- Loan Amount
- Credit Score


Click **Predict Loan Status** to instantly know whether the loan is likely to be approved.

---

# 📂 Project Structure

```
loan_model/
│
├── app.py
├── train_model.py
├── model.pkl
├── requirements.txt
├── README.md
│
├── data/
│   └── loan_data.csv
│
├── templates/
    └── index.html

```

# 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- Flask
- Joblib
- HTML5
- CSS3
- Bootstrap 5

---

# 📊 Machine Learning Workflow

The project follows these steps:

### 1. Data Collection

The dataset contains customer information required for loan approval prediction.

Examples of features include:

- Age
- Applicant Income
- Loan Amount
- Credit Score


Target Variable:

- Loan Status

---

### 2. Data Preprocessing

The preprocessing includes:

- Handling missing values
- Encoding categorical features
- Selecting important columns
- Splitting dataset into training and testing sets

```python
train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
```

---

### 3. Model Training

The project uses the **Decision Tree Classifier**.

```python
from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)
```

---

### 4. Model Evaluation

Model performance is evaluated using:

- Accuracy Score
- Confusion Matrix
- Classification Report

---

### 5. Saving the Model

```python
import joblib

joblib.dump(model, "model.pkl")
```

---

### 6. Deployment

The trained model is loaded inside Flask.

```python
model = joblib.load("model.pkl")
```

User inputs are processed and predictions are returned through a web interface.

---

# 📈 Decision Tree Visualization

The model can also be visualized using:

```python
from matplotlib import pyplot as plt
from sklearn.tree import plot_tree

plt.figure(figsize=(15,10))

plot_tree(
    model,
    feature_names=X.columns,
    class_names=model.classes_,
    filled=True
)

plt.show()
```

---

# 💻 Installation

Clone the repository

```bash
git clone https://github.com/theNERDYabhay/loan_model.git
```

Move into the project directory

```bash
cd loan_model
```

Create virtual environment (Optional)

```bash
python -m venv venv
```

Activate environment

Windows

```bash
venv\Scripts\activate
```

Linux/Mac

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

▶️ Run the Application

Train the model:

```bash
python train_model.py
```

Run Flask:

```bash
python app.py
```

Open:

```
http://127.0.0.1:5000
```

---

# Requirements
```
Flask
pandas
numpy
scikit-learn
joblib
matplotlib
```

Install them by running code:
```bash
pip install -r requirements.txt
```

---

# 📸 Screenshots
<img width="1918" height="1077" alt="image" src="https://github.com/user-attachments/assets/b44a3fde-f2a6-4852-9f23-dd9efe03dd63" />

<img width="1807" height="810" alt="image" src="https://github.com/user-attachments/assets/49df7e17-480a-48c4-a338-015fabb7a579" />

<img width="1918" height="1060" alt="image" src="https://github.com/user-attachments/assets/c3045414-385d-450a-9b11-30c9ee4856d4" />

---

# 📚 Learning Objectives

This project demonstrates:

✔ Data Cleaning

✔ Feature Engineering

✔ Train-Test Split

✔ Decision Tree Classification

✔ Model Evaluation

✔ Model Serialization

✔ Flask Deployment

---

# 🔮 Future Improvements

- Random Forest Model
- XGBoost Model
- Hyperparameter Tuning
- Feature Importance Graph
- Model Comparison
- Docker Deployment
- Cloud Deployment (Render/Heroku/AWS)

---

# 📖 Concepts Covered

- Supervised Learning
- Classification
- Decision Trees
- Machine Learning Pipeline
- Flask Deployment
- Database Management

---
Author:
ABHAY PRATAP
---
GitHub:
https://github.com/theNERDYabhay
---
If you like this project:
Give this repository a ⭐ on GitHub and feel free to contribute.
---

# 📜 License

This project is licensed under the MIT License.
