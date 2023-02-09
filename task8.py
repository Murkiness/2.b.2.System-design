#  Ковариантность 


class Person:

    def __init__(self) -> None: ...

    def say_hi(self) -> None:
        print("Hi")


class ServiceWorker(Person):

    def __init__(self) -> None:
        super().__init__()

    def say_hi(self) -> None:
        print("Greetings, customer")


def everyone_say_hi(people: 'list[Person]'):
    for p in people:
        p.say_hi()

#  Контравариантность

from typing import Callable

def make_person_clap(person: Person): ...


def let_worker_act(worker: ServiceWorker, func: Callable([ServiceWorker], None)):
    func(worker)
