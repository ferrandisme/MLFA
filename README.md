# MLFA
Machine Learning Fast Api

This project is a demo of ML models using FastAPI

# General info for all models:

- Download the dataset and rename the file to data.csv
- Add the file to the folder
- Run python -m MODEL_FOLDER.train from app


## Password Model:

This endpoint check the Strength of a password. Values:

- Weak
- Medium
- Strong

Dataset: https://www.kaggle.com/datasets/bhavikbb/password-strength-classifier-dataset

Downloaded and put it on password_model folder and renamed it to "data.csv"

#### ¿How to train the model?
From app folder:

```bash
python -m password_model.train
```
## Features

- Password Strenght ML model
- [TODO] Other ML model
- [TODO] MongoDB
- Rest API with OpenAPI



## Deployment

To deploy this project run

```bash
  python -m uvicorn main:app --reload
```

##### Warning

Docker it's not 100% configured