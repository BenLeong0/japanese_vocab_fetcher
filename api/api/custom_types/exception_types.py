import json

from api.custom_types.alternative_string_types import URL, URLField
from api.custom_types.helpers import MyBaseModel


class APIErrorDict(MyBaseModel):
    error_msg: str
    status_code: int
    url: URLField


class APIError(Exception):
    def __init__(
        self,
        error_msg: str,
        status_code: int,
        url: str | None = None,
    ):
        super().__init__(error_msg)
        self.error_msg = error_msg
        self.status_code = status_code
        self.url = URL(url or "")

    def to_dict(self) -> APIErrorDict:
        return APIErrorDict(
            status_code=self.status_code,
            error_msg=self.error_msg,
            url=self.url,
        )

    def __str__(self):
        return json.dumps(self.to_dict())
