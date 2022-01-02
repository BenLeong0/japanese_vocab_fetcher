from typing import Iterator, Optional, Pattern


class BeautifulSoup:
    text: str
    def __init__(self, markup: str, parser: str) -> None: ...
    def __getitem__(self, index: str) -> list[str]: ...
    def __iter__(self) -> Iterator[BeautifulSoup]: ...
    def find(self, name: str, class_: Optional[str]=None, id: Optional[Pattern]=None) -> BeautifulSoup: ...
    def find_all(self, name: str, class_: Optional[str] = None, id: Optional[Pattern] = None) -> list[BeautifulSoup]: ...
    def findChildren(self, name: Optional[str] = None, recursive: Optional[bool] = True) -> list[BeautifulSoup]: ...
    def findChild(self, name: Optional[str] = None) -> BeautifulSoup: ...
    def get(self, attr: str) -> str: ...