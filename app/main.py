from fastapi import FastAPI
from pydantic import BaseModel
from password_model.model import checkPassword

app = FastAPI()
version = "1.0.0" 

class Password(BaseModel):
    text: str


class PasswordStrength(BaseModel):
    strength : str


@app.get("/")
def home():
    return {"status": "Ok", "version" : version}


@app.post("/checkPassword", response_model=PasswordStrength)
def passwordCheck(password: Password):
    return  PasswordStrength(strength=checkPassword(password.text))

    
    
    
