from typing import Dict, Any
from pymongoose.mongo_types import Schema, Types

class Student(Schema):
    schema_name = "students"
    id = None
    first_name:str
    last_name:str
    def __init__(self,**kwargs):
        self.schema = {
            "first_name" : {
                "type": Types.String,
                "required" : True,
            },
            "last_name" : {
                "type": Types.String,
                "required" : True,
            },
        }
        super().__init__(self.schema_name, self.schema, kwargs)


    @classmethod
    def to_json(cls, data)->Dict[str,Any]:
        return {"_id":str(data["_id"]),"first_name":data["first_name"],"last_name":data["last_name"]}

    @classmethod
    def from_json(cls,data):
        return Student(**data)
