# Heart Disease Prediction

## Overview

This project is aimed at predicting the likelihood of heart disease in individuals based on various health metrics and clinical parameters. Heart disease is one of the leading causes of death worldwide, and early detection plays a crucial role in its management and prevention.

![Heart Image](https://drive.google.com/uc?export=view&id=1e5tAjDypuMMcniiHmzoiojsZOSB2DwpD)

## Dataset

The dataset includes the following features:

- gender: Male (1) or Female (0)

- age: Age of the individual

- education: Educational level

- currentSmoker: Whether the individual is a current smoker (1 for Yes, 0 for No)

- cigsPerDay: Average cigarettes smoked per day

- BPMeds: Whether the individual is on blood pressure medication (1 for Yes, 0 for No)

- prevalentStroke: History of stroke (1 for Yes, 0 for No)

- prevalentHyp: History of hypertension (1 for Yes, 0 for No)

- diabetes: Diabetes status (1 for Yes, 0 for No)

- totChol: Total cholesterol level (mg/dL)

- sysBP: Systolic blood pressure (mm Hg)

- diaBP: Diastolic blood pressure (mm Hg)

- BMI: Body Mass Index (kg/m²)

- heartRate: Resting heart rate (beats per minute)

- glucose: Blood glucose level (mg/dL)

- The target variable is heart disease risk (1 for at risk, 0 for no risk).

## Methodology

Data Preprocessing: The dataset was cleaned, missing values were handled, and categorical variables were encoded as necessary.

Exploratory Data Analysis (EDA): Exploratory data analysis was performed to gain insights into the distribution of variables, correlations, and potential patterns in the data.

Feature Engineering: New features were created, and existing features were transformed to improve model performance.

Model Selection: Several machine learning algorithms such as logistic regression, decision trees, random forests, and gradient boosting were trained and evaluated.

Model Evaluation: Models were evaluated using performance metrics such as accuracy, precision, recall, F1 score, and ROC-AUC to assess their predictive capabilities.

Hyperparameter Tuning: Hyperparameters of the best-performing models were fine-tuned using techniques such as grid search or random search to optimize performance further.

## Model Details

The model was trained using a Logistic Regression classifier.

Key performance metrics:

Accuracy: 85%

Precision: 82%

Recall: 84%

Hyperparameter tuning and feature engineering were applied to improve the model's performance.

## Streamlit Integration

After developing and evaluating the model, I enhanced the project by creating an interactive web-based application using Streamlit. This application enables users to:

Input key health parameters such as age, cholesterol levels, blood pressure, and BMI.

Receive predictions about the likelihood of heart disease in real time.

Visualize user inputs and predictions in an intuitive interface.

Streamlit made it easy to deploy the model and create a user-friendly platform that healthcare professionals or individuals can use effectively.

## Future Work
Incorporate additional data sources or features to enhance prediction accuracy.

Explore advanced machine learning techniques such as deep learning for improved performance.

Further refine the Streamlit application to include visualizations and analytics for better insights.

## Contributors

Arpita Goel
