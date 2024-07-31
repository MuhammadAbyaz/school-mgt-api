from typing import Dict
from http import HTTPStatus

from ...lib.exceptions.app_exception import AppException


class NotFound(AppException):
    def __init__(self,description: str | None, headers: Dict | None) -> None:
        self.http_status = HTTPStatus.NOT_FOUND
        self.reason_phrase = self.http_status.description
        super().__init__(self.reason_phrase, description, self.http_status, headers)
