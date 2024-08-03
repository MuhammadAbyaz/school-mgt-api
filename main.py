from contextlib import asynccontextmanager
from fastapi import FastAPI
from pymongo import MongoClient
from pymongoose import set_schemas

from .model.student import Student
from .api import v1
from .lib.db.database import connectToDB
from dotenv import dotenv_values
config = dotenv_values(".env")

@asynccontextmanager
async def lifespan(app:FastAPI):
    if config["DB_URL"] and config["DB_NAME"]:
        app.mongodb_client: MongoClient = connectToDB(config["DB_URL"])
        app.database = app.mongodb_client[config["DB_NAME"]]
        schemas = {
            "students": Student().schema
        }
        set_schemas(app.database,schemas)
        yield
        app.mongodb_client.close()
    
app = FastAPI(lifespan=lifespan)
app.include_router(router=v1.router)


@app.get("/healthcheck")
def healthCheck() -> str:
    return "RUNNING"
