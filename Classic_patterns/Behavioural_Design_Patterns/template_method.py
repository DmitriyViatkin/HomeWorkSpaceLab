from abc import ABC, abstractmethod
from typing import List


class Pizza:
    def __init__(self):
        self.__state: List[str] = ['base']

    def add_ingredient(self,ingredient):
        print(f"Add in pizza: {ingredient}")
        self.__state.append(ingredient)

    def __str__(self):
        return f"Ingredient pizza:{self.__state}"


class PizzaMaker(ABC):
    def make_pizza(self,pizza: Pizza):
        self.prepare_sauce(pizza)
        self.prepare_topping(pizza)
        self.cook(pizza)

    @abstractmethod
    def prepare_sauce(self, pizza: Pizza):
        pass

    @abstractmethod
    def prepare_topping(self, pizza: Pizza):
        pass

    @abstractmethod
    def cook(self, pizza: Pizza):
        pass


class MargaritaMaker(PizzaMaker):
    """Класс приготовления пиццы Маргарита"""
    def prepare_sauce(self, pizza: Pizza) -> None:
        pizza.add_ingredient('Tomato')

    def prepare_topping(self, pizza: Pizza) -> None:
        pizza.add_ingredient('Bacon')
        pizza.add_ingredient('Mozzarella')
        pizza.add_ingredient('Mozzarella')

    def cook(self, pizza: Pizza) -> None:
        print("Пицца 'Маргарита' будет готова через 10 минут")


class Chief:
    """Класс шеф-повара"""
    def __init__(self, template_pizza: PizzaMaker):
        self.__cook = template_pizza

    def set_cook_template(self, template_pizza: PizzaMaker):
        self.__cook = template_pizza

    def make_pizza(self) -> Pizza:
        pizza = Pizza()
        self.__cook.make_pizza(pizza)
        return pizza


if __name__ == "__main__":
    chief = Chief(MargaritaMaker())
    print("*"*8 + "Готовим пиццу 'Маргарита'"+8*"*")
    print(chief.make_pizza())
