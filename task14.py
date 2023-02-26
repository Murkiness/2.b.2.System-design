from typing import List, TypeVar, Union


class General:
    pass


GeneralT = TypeVar('GeneralT', bound=General)
T = TypeVar('T')


class Vector:

    def __init__(self, values: List[GeneralT]) -> None:
        self.values = values

    def __add__(self, other: "Vector[T]") -> Union["Vector[T]", None]:
        if len(self.values) != len(other.values):
            return None
        return Vector([x + y for x, y in zip(self.values, other.values)])