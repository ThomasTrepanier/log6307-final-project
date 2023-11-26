from collections.abc import MutableMapping
from typing import Any, Iterator

from pydantic import BaseModel


class BaseModelDict(BaseModel, MutableMapping):
    """Goodness of BaseModel and acts like a dictionary."""

    def __contains__(self, x: str) -> bool:
        return True if x in self.__dict__.keys() else False

    def __delitem__(self, x: str) -> None:
        del self.__dict__[x]

    def __getitem__(self, x: str) -> Any:
        return self.__dict__[x]

    def __iter__(self) -> Iterator:
        return iter(self.__dict__)

    def __json__(self) -> dict:
        return self.__dict__

    def __len__(self) -> int:
        return len(self.__dict__)

    def __setitem__(self, key: str, value: Any) -> None:
        self.__dict__[key] = value
