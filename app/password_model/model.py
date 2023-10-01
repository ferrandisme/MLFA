import pickle
from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent

def word(password):
    character = []
    for i in password:
        character.append(i)
    return character

with open(f"{BASE_DIR}/password_security_model.pkl", "rb") as f:
    model = pickle.load(f)
with open(f"{BASE_DIR}/vector.pkl", "rb") as f:
    tdif, _ = pickle.load(f) 

def checkPassword(password):
    password_vectorized = tdif.transform([password]) 
    return model.predict(password_vectorized)[0]
 