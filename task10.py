'''
При помощи final можно обозначить метод как закрытый для переопределения в классах потомках,
но фактически в силу динаминической природы языка переопределить метод можно.
Также не помогают метаклассы.
'''


from typing import final


class Person:

    def __init__(self) -> None: ...

    @final
    def say_hi(self) -> None:
        print("Hi")


class Butler(Person):

    def __init__(self) -> None:
        super().__init__()

    def say_hi(self) -> None:
        print("Greetings, sir")
