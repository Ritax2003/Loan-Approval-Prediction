# Loan Approval Prediction System

Welcome to the Loan Approval Prediction System! This project uses machine learning models to predict loan approval status based on various applicant features. The application is deployed using Streamlit and is accessible via - Streamlit Link-  [this link](https://loan-approval-prediction-subrata.streamlit.app/).
### This file is also uploaded in Huggingface space - https://huggingface.co/spaces/subrata2003/loan_approval_system

## Project Overview

The Loan Approval Prediction System is designed to assist financial institutions in predicting whether a loan application will be approved or not. The system uses logistic regression and decision tree models to analyze applicant information and provide a prediction.

## Features

- **User-Friendly Interface:** Built with Streamlit for an interactive web application experience.
- **Predictive Models:** Utilizes logistic regression and decision tree models.
- **Dynamic Predictions:** Real-time predictions based on user input.
- **GitHub Integration:** Hosted on GitHub for version control and collaboration.

## How It Works

1. **Input Data:** Users provide details about the loan applicant, including personal and financial information.
2. **Model Prediction:** The backend processes the input data using pre-trained machine learning models.
3. **Output:** The system displays the predicted loan approval status.

## Models Used

- **Logistic Regression:** Accuracy: 89.80%
- **Decision Tree:** Accuracy: 79.55%

## Getting Started

To run this project locally, follow these steps:

**Clone the Repository**

   ```bash
   git clone https://github.com/your-username/loan-approval-prediction.git
   cd loan-approval-prediction

   ## Install Dependencies

Ensure you have Python 3.7+ installed. Then, create a virtual environment and install the required packages:

```bash
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
pip install -r requirements.txt

## Run the application
streamlit run app.py

