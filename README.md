# Loan Prediction using Logistic Regression

This project uses a loan prediction dataset to perform data cleaning, exploratory data analysis (EDA), and builds a logistic regression model to predict loan approval.

## Table of Contents
- Project Overview
- Requirements
- Dataset
- [Data Preprocessing
- Exploratory Data Analysis 
- Modeling
- Evaluation
- Results

## Project Overview
The objective of this project is to predict the loan approval status of applicants based on various factors like gender, marital status, education, employment status, and credit history using logistic regression.

## Requirements
To run this project, you need the following Python libraries:

```
pip install numpy pandas matplotlib seaborn scikit-learn
```

## Dataset

The dataset used is train.csv which contains the following columns:

- Gender
-	Married
-	Dependents
-	Education
-	Self_Employed
-	Property_Area
-	LoanAmount
-	Loan_Amount_Term
-	Credit_History
-	Loan_Status

The target variable is Loan_Status, where ‘Y’ represents loan approval and ‘N’ represents rejection.

## Data Preprocessing

1.	Handling Missing Values:
-	Missing values in LoanAmount were filled with the mean.
-	Missing values in Credit_History were filled with the median.
-	Remaining missing values were removed.
  
2.	Label Encoding:
Categorical variables were converted to numerical values:
-	Gender: Male = 1, Female = 0
-	Married: Yes = 1, No = 0
-	Dependents: ‘0’ = 0, ‘1’ = 1, ‘2’ = 2, ‘3+’ = 3
-	Education: Graduate = 1, Not Graduate = 0
-	Self_Employed: Yes = 1, No = 0
-	Property_Area: Urban = 2, Semiurban = 1, Rural = 0
-	Loan_Status: Y = 1, N = 0

## Exploratory Data Analysis (EDA)

The dataset was visualized using count plots to observe the distribution of categorical variables such as:

-	Gender vs Loan_Status
-	Married vs Loan_Status
-	Education vs Loan_Status
-	Self_Employed vs Loan_Status
-	Property_Area vs Loan_Status

## Modeling

-	Model: Logistic Regression
-	Features: Independent variables like gender, marital status, education, etc.
-	Target: Loan_Status (0 or 1)

The data was split into training and testing sets using an 70-30 split. A logistic regression model was trained on the training set and used to predict loan approval on the testing set.

## Evaluation

The performance of the logistic regression model was evaluated using:

-	Accuracy Score
-	Confusion Matrix
-	Precision
-	Recall
-	F1-Score

## Results

The logistic regression model achieved an accuracy score, along with precision, recall, and F1-score.

```
Precision = 0.7591240875912408
Recall = 0.9811320754716981
F1 Score = 0.8559670781893004
```

## Conclusion

This project demonstrates the process of predicting loan approval using logistic regression. Data cleaning, EDA, and proper feature encoding were critical in building a successful model. Further improvements could include using other classification models and hyperparameter tuning to increase prediction accuracy.
