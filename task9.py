import pickle
from copy import deepcopy
from typing import TypeVar, final

T = TypeVar('T')


class General(object):

    def __init__(self, **kwargs) -> None: ...

    @final
    def copy(self, other: T) -> None:
        other.__dict__ = deepcopy(self.__dict__)

    @final
    def clone(self) -> T:
        return deepcopy(self)

    @final
    def serialize(self) -> bytes:
        return pickle.dumps(self)

    @final
    @staticmethod
    def deserialize(serialized_obj: bytes) -> T:
        return pickle.loads(serialized_obj)

    @final
    def is_type(self, classtype) -> bool:
        return type(self) == classtype

    @final
    def type(self):
        return self.__class__.__name__

    @final
    def attributes(self) -> str:
        return f'attributes: {self.__dict__}'

    @final
    def __eq__(self, other: T) -> bool:
        return self.__dict__ == other.__dict__


class Any(General):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.__dict__ = kwargs