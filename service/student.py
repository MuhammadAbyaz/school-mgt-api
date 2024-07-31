from typing import List, Dict

from pydantic import ValidationError

from ..dto.student.updateStudent import UpdateStudent

from ..dto.student.createStudent import CreateStudent
from ..repository.student import StudentRepository
from ..model.student import Student


class StudentService:
    def __init__(self) -> None:
        self.student_repository = StudentRepository()
    def find_all(self)->List[Dict]:
        return self.student_repository.find();
    def find_by_id(self,id)->Dict:
        return self.student_repository.find_one(id)
    def insert(self,data:Dict)->str | Dict:
        try:
           student_dto = CreateStudent(**data)
           return self.student_repository.insert(Student(first_name=student_dto.first_name,last_name=student_dto.last_name))
        except ValidationError as e:
            return {"fields": [error["loc"][0] for error in e.errors()], "messages": [error["msg"] for error in e.errors()]}
    def update(self,id:int,data:Dict)->str|Dict:
        student_data = self.student_repository.find_one(id)
        if student_data:
            try:
                updated_student = UpdateStudent(**{**student_data, **data})
                return self.student_repository.update(id,updated_student.to_json())
            except ValidationError as e:
                return {"fields": [error["loc"][0] for error in e.errors()], "messages": [error["msg"] for error in e.errors()]}

