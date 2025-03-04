from __future__ import annotations

from abc import ABC, abstractmethod
from enum import Enum
from typing import List


class WorkerType(Enum):

    Plumber = 1
    Electrician = 2
    Admin = 3

class IMediator(ABC):

    @abstractmethod
    def notify(self, emp : 'Emploee', msg: str):
        pass


class Emploee(ABC):
    def __init__(self, mediator: IMediator):
        self._mediator = mediator

    def set_mediator(self, med: IMediator):
        self._mediator = med

class Plumber(Emploee):
    def __init__(self, med:IMediator = None):
        super().__init__(med)
        self.__is_working = False

    def execute_work(self):
        print('<Чиним водопровод>')
        self._mediator.notify(self, "Чиним водопровод")

    def set_work(self, state: bool):
        self.__is_working = state
        if state:
            print("Сантехник свободен")
        else:
            print("Водопровод всё ещё порван")


class Electrician(Emploee):
    def __init__(self, med: IMediator = None):
        super().__init__(med)
        self.__is_working = False

    def execute_work(self):
        print('<Чиним трансформатор>')
        self._mediator.notify(self, "Чиним трансформатор")

    def set_work(self, state: bool):
        self.__is_working = state
        if state:
            print("Электрик  свободен")
        else:
            print("Провода всё ещё оборваны")


class Administration(Emploee):
    def __init__(self,med:IMediator = None):
        super().__init__(med)
        self.__text: str = None

    def give_command(self,txt: str):
        self.__text = txt
        if txt == "":
            print("Админ  вкурсе что делпет")
        else:
            print("Админ говорит: " + txt)
        self._mediator.notify(self,txt)

    def set_work(self, state: bool):
        self.__command_given = state
        if state:
            print("Админ дал команду")
        else:
            print("Админ ожидает команду")


class Controller (IMediator):
    def __init__(self, plumber: Plumber, electrician: Electrician, admin: Administration):
        self.__plumber = plumber
        self.__electrician = electrician
        self.__admin = admin
        plumber.set_mediator(self)
        electrician.set_mediator(self)
        admin.set_mediator(self)
        """self.workers = {WorkerType.Electrician:[],
                        WorkerType.Plumber:[],
                        WorkerType.Admin:[]}"""
    """def add_worker(self, worker: Emploee):
        if worker not in self.workers[worker.type()]:
            (self.workers[worker.type()].append(worker))

    def remove_worker(self, worker: Emploee):
        if worker not in self.workers[worker.type()]:
            (self.workers[worker.type()].remove(worker))"""

    def notify(self, emp : 'Emploee', msg: str):
        if isinstance(emp, Administration):
            if msg == 'Электрик':
                self.__electrician.set_work(True)
            else:
                self.__electrician.set_work(False)

        if isinstance(emp, Plumber):
            if msg == 'Вода':
                self.__plumber.set_work(True)
            else:
                self.__plumber.set_work(False)

        if isinstance(emp, Administration):
            if msg == '':
                self.__admin.set_work(True)
            else:
                self.__admin.set_work(False)

if __name__ == "__main__":

    plumber = Plumber()
    electrician = Electrician()
    admin = Administration()

    mediator = Controller(plumber,electrician,admin)
    admin.give_command("Водопровод")
    print()
    plumber.execute_work()
    admin.give_command("Электрик")