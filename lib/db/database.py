from pymongo import MongoClient


def connectToDB(db_url:str):
    try:
        client = MongoClient(db_url)
        return client
    except Exception as e:
        print(e)
