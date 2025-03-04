from abc import ABC, abstractmethod
from typing import List,Deque


class ICommand(ABC):
    """Базовій класс команд"""
    @abstractmethod
    def execute(self):
        pass

class CoffeeMaker:

    def on(self):
        print("Кофеварка запущена")

    def heating(self):
        print("Кофе будет подогреваться")

    def off(self):
        print("Кофеварка будет отключена ")


class CoffeeMakerCommand(ICommand):
    def __init__(self,maker:CoffeeMaker):
        self.maker: CoffeeMaker = maker

    def turn_on(self):
        self.maker.on()

    def turn_off(self):
        self.maker.off()

    def execute(self):
        self.maker.heating()

class CoffeeAdjustCommand(ICommand):
    def __init__(self,maker:CoffeeMaker):
        self.maker:CoffeeMakerCommand = maker

    def turn_on(self):
        self.maker.turn_on()

    def turn_heating(self):
        self.maker.execute()

    def turn_off(self):
        self.maker.turn_off()





class MakerPult:
    def __init__(self,number_of_buttons: int):
        self.__commands: List[ICommand] = [None] * number_of_buttons
        self.__history: Deque[ICommand] = []

    def set_command(self, button: int, command:ICommand):
        self.__commands[button] = command

    def press_on(self, button: int):
        self.__commands[button].turn_on()
        self.__history.append(self.__commands[button])

    def press_execute(self, button: int):
        if button < len(self.__commands) and self.__commands[button]:
            self.__commands[button].execute()
            self.__history.append(self.__commands[button])
        else:
            print(f"Команда для кнопки {button} не установлена.")

    def press_cancel(self):
        if self.__history:
            command = self.__history.pop()
            command.turn_off()
        else:
            print("Нет команд для отмены.")

if __name__ == "__main__":

    maker = CoffeeMaker()
    makerpult = MakerPult(number_of_buttons=3)

    makerpult.set_command(0, CoffeeMakerCommand(maker))
    makerpult.set_command(1, CoffeeMakerCommand(maker))
    makerpult.set_command(2, CoffeeMakerCommand(maker))


    makerpult.press_on(0)
    makerpult.press_execute(1)
    makerpult.press_on(2)

    makerpult.press_cancel()
