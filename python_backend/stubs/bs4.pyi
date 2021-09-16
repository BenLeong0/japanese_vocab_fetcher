from typing import List, Optional, Pattern


class BeautifulSoup:
    text: str

    def __init__(self, markup: str, parser: str):
        ...

    def find(self, name: str, class_: Optional[str]=None, id: Optional[Pattern]=None) -> BeautifulSoup:
        ...

    def find_all(self, name: str, class_: Optional[str] = None, id: Optional[Pattern] = None) -> List[BeautifulSoup]:
        ...

    def findChildren(self, name: Optional[str] = None, recursive: Optional[bool] = True) -> List[BeautifulSoup]:
        ...

    def findChild(self, name: Optional[str] = None) -> BeautifulSoup:
        ...

    def get(self, attr: str) -> str:
        ...


class PageElement:
    ...
