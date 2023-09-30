from fastapi import FastAPI
from pydantic import BaseModel
from password_model.model import checkPassword

app = FastAPI()
version = "1.0.0" 

class Password(BaseModel):
    text: str


class PasswordStrength(BaseModel):
    strength : str


@app.get("/status")
async def status():
    return {"status": "Ok", "version" : version}


@app.post("/checkPassword", response_model=PasswordStrength)
async def status(password: Password):
    print("CONTRASEÑA" , password)
    return  PasswordStrength(strength=checkPassword(password.text))

    
    
    
