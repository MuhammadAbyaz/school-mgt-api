from typing import Dict
from http import HTTPStatus
from ...lib.exceptions.app_exception import AppException


class InternalServerError(AppException):
    def __init__(self,description: str | None, headers: Dict | None) -> None:
        self.http_status = HTTPStatus.INTERNAL_SERVER_ERROR
        self.reason_phrase = self.http_status.description
        super().__init__(self.reason_phrase, description, self.http_status, headers)
