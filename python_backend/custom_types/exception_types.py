import json
from typing import Literal, TypedDict

from custom_types.alternative_string_types import URL


class APIErrorDict(TypedDict):
    error_msg: str
    status_code: int
    url: URL


class APIError(Exception):
    def __init__(
        self,
        error_msg: str,
        status_code: int,
        url: URL = URL(""),
    ):
        super().__init__(error_msg)
        self.error_msg = error_msg
        self.status_code = status_code
        self.url = url


    def to_dict(self) -> APIErrorDict:
        return {
            "status_code": self.status_code,
            "error_msg": self.error_msg,
            "url": self.url,
        }


    def __str__(self):
        return json.dumps(self.to_dict())


class FailedResponseItem(TypedDict):
    success: Literal[False]
    error: APIErrorDict


def api_error_response_factory(api_error: APIError) -> FailedResponseItem:
    return {
        "success": False,
        "error": api_error.to_dict(),
    }
