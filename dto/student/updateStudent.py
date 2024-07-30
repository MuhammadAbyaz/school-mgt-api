from pydantic import BaseModel, Field
from typing import Dict, Optional


class UpdateStudent(BaseModel):
    first_name: Optional[str] = Field(min_length=3, max_length=10)
    last_name: Optional[str] = Field(min_length=3, max_length=10)
    
    def to_json(self)->Dict:
            return {"first_name":self.first_name, "last_name": self.last_name}
