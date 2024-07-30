from pydantic import BaseModel,Field
class CreateStudent(BaseModel):
    first_name: str = Field(min_length=3, max_length=8)
    last_name: str = Field(min_length=3, max_length=10)
