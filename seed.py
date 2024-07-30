from pymongo import MongoClient
def seed():
    client = MongoClient("mongodb://admin:admin@localhost:27017/school_database?authSource=admin")
    db = client.school_database
    data = [{"first_name": "Muhammad Abyaz", "last_name": "Khalid"}, {"first_name": "Muhammad Hasham", "last_name": "Khalid"}]
    db.students.insert_many(doc for doc in data)
    client.close()

seed()
