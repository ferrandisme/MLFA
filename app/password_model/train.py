import pandas as pd
import numpy as np
import pickle

from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from .token_utils import word

BASE_DIR = Path(__file__).resolve(strict=True).parent

print("Started model preparation")
data = pd.read_csv(f"{BASE_DIR}/data.csv", on_bad_lines="skip")
# delete null values in any column
data = data.dropna()
# change 0,1,2 to weak, medium, strong
data["strength"] = data["strength"].map({0: "Weak", 
                                         1: "Medium",
                                         2: "Strong"})

x = np.array(data["password"])
y = np.array(data["strength"])

print("Tokenize data")
tdif = TfidfVectorizer(tokenizer=word)
x = tdif.fit_transform(x)
print("Vector fit")

with open(f"{BASE_DIR}/vector.pkl",'wb') as f:
    pickle.dump((tdif,word),f)
print("Vector Saved")

xtrain, xtest, ytrain, ytest = train_test_split(x, y, 
                                                    test_size=0.1, 
                                                    random_state=25)

print("Starting training...")
model = RandomForestClassifier()
model.fit(xtrain, ytrain)
print("Accuracy: " , model.score(xtest, ytest))
# the current accuracy with this parameters is of 0.9560659458813691

with open(f"{BASE_DIR}/password_security_model.pkl",'wb') as f:
    pickle.dump(model,f)

print("Model saved. Process ended")


