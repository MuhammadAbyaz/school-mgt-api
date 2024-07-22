from fastapi import FastAPI
from api import v1
app = FastAPI()

app.include_router(v1.router)

@app.get("/healthCheck")
def healthCheck()-> str:
    return "RUNNING" 
