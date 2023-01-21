from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')


class Weapon:

    # Конструктор
    # постусловие: создано оружием с указанной прочностью и уроном
    def __init__(self, durability: int, damage: int) -> None:
        self.durability = durability
        self.damage = damage

    #  Запросы
    def get_damage(self) -> int:
        return self.damage

    def get_durability(self) -> int:
        return self.durability


class Player(ABC, Generic[T]):

    # Конструктор
    # постусловие: создан игрок с указанным именем
    def __init__(self, name: str) -> None: ...

    # Запросы
    @abstractmethod
    def info(self) -> str: ...  # Возвращает информацию об игроке


# Пример наследования, полиморфизма и композиции
class Warrior(Player):

    # Конструктор
    # постусловие: создан персонаж класса Warrior с указанным именем
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.weapon: Weapon = None  # композиция

    # Запросы
    @abstractmethod
    def info(self) -> str: ...  # Возвращает информацию об персонаже (полиморфизм)
