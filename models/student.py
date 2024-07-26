from pymongoose.mongo_types import Schema, Types


class Student(Schema):
    schema_name = "students"
    id = None
    def __init__(self):
        self.schema = {
            "firstName" : {
                "type": Types.String,
                "required" : True,
            },
            "lastName" : {
                "type": Types.String,
                "required" : True,
            },
        }
        super().__init__(self.schema_name, self.schema)


