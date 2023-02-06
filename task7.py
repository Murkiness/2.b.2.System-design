from abc import ABC, abstractmethod


class Player(ABC):

    def __init__(self, damage: int) -> None:
        self.damage = damage

    @abstractmethod
    def get_damage() -> int: ...


class Healer(Player):

    def __init__(self, damage: int) -> None:
        super().__init__(damage)

    def get_damage(self) -> int:
        return self.damage


class Warrior(Player):

    def __init__(self, damage: int) -> None:
        super().__init__(damage)

    def get_damage(self) -> int:
        return self.damage * 2

# В зависимости от класса, damage будет вычислен по своей формуле
if __name__ == '__main__':
    players = [Warrior(7), Healer(3)]
    for p in players:
        print(p.get_damage())
