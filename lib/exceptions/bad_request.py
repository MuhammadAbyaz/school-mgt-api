from typing import Dict
from http import HTTPStatus
from ...lib.exceptions.app_exception import AppException


class BadRequest(AppException):
    def __init__(self,description:str|None,headers:Dict|None) -> None:
        self.http_code = HTTPStatus.BAD_REQUEST
        self.reason_phrase = self.http_code.description
        super().__init__(self.reason_phrase,description,self.http_code,headers)
