from typing import List

class Player:

    def special_action(self):
        print("No special action")


class Warrior(Player):

    def special_action(self):
        print("Attack")


class Priest(Player):

    def special_action(self):
        print("Heal")


# ковариантная функция, входной типа список объектов класса Player, может принимать и подтипы.
def make_special_actions(players: List[Player]):
    for p in players:
        p.special_action()

# метод special_action является полиморфным поскольку он переопределен в классах потомках и поведение меняется
# в зависимости от вызывающего объекта
