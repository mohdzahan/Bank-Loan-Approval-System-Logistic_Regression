# Loan Status Predictor

## Overview
This is a Flask based web application that predicts loan approval status based on user input. The application uses a pre trained machine learning model (`loan_model.pkl`) to make predictions based on features such as gender, marital status, income, loan amount, and more. The frontend is styled using Tailwind CSS for a clean and responsive user interface.

## Features
- Input form to collect user details such as Gender, Married status, Dependents, Education, and more.
- Prediction of loan approval status (Approved or Not Approved).
- Responsive UI styled with Tailwind CSS.
- Error handling for missing model file or invalid inputs.

## Screenshot
<p align='center'>
<img src="Loan Status .PNG" width=600>
</p>


## Prerequisites
- Python 3.8+
- Flask
- NumPy
- Joblib
- A pre trained machine learning model (`loan_model.pkl`)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/mohdzahan/Bank-Loan-Approval-System-Logistic_Regression
   cd loan-status-predictor
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  
   ```
3. Install the required dependencies:
   ```bash
   pip install flask numpy joblib
   ```
4. Ensure the `loan_model.pkl` file is in the project root directory.
5. Place a screenshot of the UI in the project root directory as `screenshot.png` (optional, for README display).

## Usage
1. Run the Flask application:
   ```bash
   python app.py
   ```
2. Open a web browser and navigate to `http://127.0.0.1:5000/`.
3. Fill out the form with the required details and click "Predict Loan Status" to see the prediction result.

## Project Structure
```
loan-status-predictor/
│
├── app.py                  # Flask application script
├── loan_model.pkl          # Pre trained machine learning model
├── templates/
│   └── index.html          # HTML template for the UI
├── Loan Status .PNG          # Screenshot of the UI  
└── README.md               # This file
```

## Notes
- The `loan_model.pkl` file must be a valid pre trained model compatible with the input features used in `app.py`.
- The application uses a simple form submission. Due to sandbox restrictions, avoid using `<form>` with `onSubmit` in production environments; this implementation uses a POST request to the root route.
