from fastapi import FastAPI

app = FastAPI()
version = "1.0.0" 


@app.get("/status")
async def status():
    return {"status": "Ok", "version" : version}


    
    
    
