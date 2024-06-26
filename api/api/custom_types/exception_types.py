import json
from typing import TypedDict

from api.custom_types.alternative_string_types import URL


class APIErrorDict(TypedDict):
    error_msg: str
    status_code: int
    url: URL


class APIError(Exception):
    def __init__(
        self,
        error_msg: str,
        status_code: int,
        url: URL | None = None,
    ):
        super().__init__(error_msg)
        self.error_msg = error_msg
        self.status_code = status_code
        self.url = url or URL("")

    def to_dict(self) -> APIErrorDict:
        return {
            "status_code": self.status_code,
            "error_msg": self.error_msg,
            "url": self.url,
        }

    def __str__(self):
        return json.dumps(self.to_dict())
