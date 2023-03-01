from abc import abstractmethod, ABC


class Player(ABC):

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def special_action(self):
        pass


class Warrior(Player):

    def __init__(self, name: str):
        super().__init__(name)


    def special_action(self):
        print("Attack")


class Priest(Player):

    def __init__(self, name: str):
        super().__init__(name)


    def special_action(self):
        print("Heal")
