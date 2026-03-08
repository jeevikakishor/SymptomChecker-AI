# SymptomChecker-AI

AI Medical Symptom Checker is a machine learning-based web application that predicts possible diseases based on symptoms selected by the user.

The application uses a Random Forest machine learning model trained on a symptom dataset to provide the top 3 possible disease predictions along with recommended precautions.

## Features

- Symptom selection using searchable dropdown menus
- AI-based disease prediction
- Displays top 3 probable diseases with probability
- Provides precaution suggestions
- Simple web interface built with Flask
- Deployable on Render

## Technologies Used

- Python
- Flask
- Scikit-learn
- Pandas
- HTML / CSS
- Select2 (for searchable dropdown)

## How It Works

1. The user selects symptoms from dropdown menus.
2. The system sends the symptoms to a trained machine learning model.
3. The model predicts possible diseases based on symptom patterns.
4. The application displays the top predictions and recommended precautions.

## Use Case

This project demonstrates how machine learning can be used in healthcare applications to assist in preliminary disease prediction based on symptoms.
