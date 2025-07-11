
from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)
try:
    model = joblib.load('loan_model.pkl')
except FileNotFoundError:
    print("Error: loan_model.pkl not found. Please ensure it is in the same directory.")
    exit(1)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    form_data = {}
    if request.method == 'POST':
        try:
            form_data = {
                'Gender': request.form.get('Gender', 'Male'),
                'Married': request.form.get('Married', 'No'),
                'Dependents': request.form.get('Dependents', '0'),
                'Education': request.form.get('Education', 'Graduate'),
                'Self_Employed': request.form.get('Self_Employed', 'No'),
                'ApplicantIncome': request.form.get('ApplicantIncome', ''),
                'CoapplicantIncome': request.form.get('CoapplicantIncome', ''),
                'LoanAmount': request.form.get('LoanAmount', ''),
                'Loan_Amount_Term': request.form.get('Loan_Amount_Term', ''),
                'Credit_History': request.form.get('Credit_History', '1'),
                'Property_Area': request.form.get('Property_Area', 'Urban')
            }
            inputs = [
                1 if form_data['Gender'] == 'Male' else 0,
                1 if form_data['Married'] == 'Yes' else 0,
                int(form_data['Dependents'].replace('3+', '3')) if form_data['Dependents'] else 0,
                1 if form_data['Education'] == 'Graduate' else 0,
                1 if form_data['Self_Employed'] == 'Yes' else 0,
                float(form_data['ApplicantIncome']) if form_data['ApplicantIncome'] else 0,
                float(form_data['CoapplicantIncome']) if form_data['CoapplicantIncome'] else 0,
                float(form_data['LoanAmount']) if form_data['LoanAmount'] else 0,
                float(form_data['Loan_Amount_Term']) if form_data['Loan_Amount_Term'] else 0,
                float(form_data['Credit_History']) if form_data['Credit_History'] else 0,
                2 if form_data['Property_Area'] == 'Urban' else 1 if form_data['Property_Area'] == 'Semiurban' else 0
            ]
            inputs = np.array(inputs).reshape(1, -1)
            prediction = model.predict(inputs)[0]
            prediction = 'Approved' if prediction == 1 else 'Not Approved'
        except Exception as e:
            prediction = f'Error: {str(e)}'
    return render_template('index.html', prediction=prediction, form_data=form_data)

if __name__ == '__main__':
    app.run(debug=True)
