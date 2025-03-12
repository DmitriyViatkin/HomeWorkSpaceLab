from abc import ABC, abstractmethod
from typing import List, Deque
from collections import deque

class ICommand(ABC):
    """Базовый класс команд"""
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

class CoffeeMaker:
    def on(self):
        print("Кофеварка запущена")

    def heating(self):
        print("Кофе подогревается")

    def off(self):
        print("Кофеварка выключена")

class CoffeeCommand(ICommand):
    def __init__(self, maker: CoffeeMaker, action: str):
        self.maker = maker
        self.action = action

    def execute(self):
        if self.action == "on":
            self.maker.on()
        elif self.action == "heating":
            self.maker.heating()
        elif self.action == "off":
            self.maker.off()

    def undo(self):
        if self.action == "on":
            self.maker.off()
        elif self.action == "heating":
            pass # Нельзя отменить нагрев
        elif self.action == "off":
            self.maker.on()

class MakerPult:
    def __init__(self, number_of_buttons: int):
        self.commands: List[ICommand] = [None] * number_of_buttons
        self.history: Deque[ICommand] = deque()

    def set_command(self, button: int, command: ICommand):
        self.commands[button] = command

    def press_button(self, button: int):
        if self.commands[button]:
            self.commands[button].execute()
            self.history.append(self.commands[button])
        else:
            print(f"Команда для кнопки {button} не установлена.")

    def press_undo(self):
        if self.history:
            command = self.history.pop()
            command.undo()
        else:
            print("Нет команд для отмены.")

if __name__ == "__main__":
    maker = CoffeeMaker()
    pult = MakerPult(number_of_buttons=3)

    pult.set_command(0, CoffeeCommand(maker, "on"))
    pult.set_command(1, CoffeeCommand(maker, "heating"))
    pult.set_command(2, CoffeeCommand(maker, "off"))

    pult.press_button(0)  # Включить
    pult.press_button(1)  # Подогреть
    pult.press_button(2)  # Выключить

    pult.press_undo()      # Отменить выключение
    pult.press_undo()      # Отменить подогрев (нельзя)
    pult.press_undo()