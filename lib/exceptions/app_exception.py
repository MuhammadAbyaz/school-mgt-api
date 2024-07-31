from http import HTTPStatus
from typing import Dict
class AppException(Exception):
    def __init__(self,name:str,description:str|None,status_code:int,headers:Dict|None) -> None:
        self.name = name
        self.status_code = status_code
        self.description = list(status.description for status in HTTPStatus if status.value == self.status_code)[0] if not description else description
        self.headers = headers
        super().__init__(self.description)
