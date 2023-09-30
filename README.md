# MLFA
Machine Learning Fast Api

This project is a demo of ML models using FastAPI

# How to deploy the app:

python -m uvicorn main:app --reload

# General info for all models:

1- download the dataset and rename the file to data
2- add the file to the folder
3- run train.py and wait

## Password Model:

This endpoint check the Strength of a password. Values:

- Weak
- Medium
- Strong

Dataset: https://www.kaggle.com/datasets/bhavikbb/password-strength-classifier-dataset

¿How to train the model?
From app folder:
python -m password_model.train


