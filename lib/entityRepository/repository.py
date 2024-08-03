from typing import Dict, List


class RepositoryInterface():
    def __init__(self,model) -> None:
        self.model = model
    def find(self)->List[Dict]:
        return [self.model.to_json(doc) for doc in self.model.find({},parse=False)]
    def find_one(self,id:str)->Dict:
        return self.model.to_json(self.model.find_one({"_id":id},parse=False))
    def insert(self,model)->str:
        return str(model.save())
    def update(self,id:str,data:Dict)->str:
        self.model.update({"_id":id},{
            "$set":{**data}
        })
        return str(id)
