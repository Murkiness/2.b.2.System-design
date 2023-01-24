class Person:

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def get_name(self) -> str:
        return self.name


class SecretAgent(Person):

    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)

    # Специализация класса-родителя - метод переопределён
    def get_name(self) -> str:
        return "fake name"


class Player(Person):

    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)

    # Расширение класса-родителя методом которого нет в родительском классе
    def send_message(self, other_player_name: str) -> None: ...
