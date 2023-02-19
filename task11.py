import os
import sys
files_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(files_dir))


from typing import final


from task9 import Any


class A(Any):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)


class B(Any):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)


@final
class NoneType(A, B):

    @final
    def __new__(cls, **kwargs):
        return None


if __name__ == "__main__":
    a: A = A(text="abc")
    b: B = B(text="bcd")
    t: Any = NoneType()

    for o in [a, b, t]:
        if o is None:
            continue
        print(o.attributes())