from fastapi import FastAPI
from .api import v1
from .lib.db.database import connectToDB

app = FastAPI()
connectToDB("mongodb://localhost:27017/schoolDatabase")
app.include_router(router=v1.router)

@app.get("/healthcheck")
def healthCheck() -> str:
    return "RUNNING"
