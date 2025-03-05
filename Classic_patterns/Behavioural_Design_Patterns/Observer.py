from abc import  ABC, abstractmethod
from typing import List

class IObserver (ABC):
    @abstractmethod
    def update(self,p):
        pass


class IObservable(ABC):
    @abstractmethod
    def add_observer(self,o:IObserver):
        pass

    @abstractmethod
    def remove_observer(self,o:IObserver):
        pass

    @abstractmethod
    def notify(self):
        pass


class Product(IObservable):
    def __init__(self, price:int):
        self.__price = price
        self.__observers:List[IObserver] = []

    def change_price(self, price):
        self.__price = price
        self.notify()

    def add_observer(self,o:IObserver):
        self.__observers.append(o)

    def remove_observer(self,o:IObserver):
        self.__observers.remove(o)

    def notify(self):
        for o in self.__observers:
            o.update(self.__price)


class Wholesale(IObserver):
    def __init__(self, obj: IObservable):
        self.__product = obj
        obj.add_observer(self)

    def update(self, p:int):
        if p<300:
            print(f"Товар закуплен по {p}")
            self.__product.remove_observer(self)


class Buyer (IObserver):
    def __init__(self, obj: IObservable):
        self.__product = obj
        obj.add_observer(self)

    def update(self, p:int):
        if p<350:
            print(f"Товар закуплен по {p}")
            self.__product.remove_observer(self)


if __name__ == "__main__":

    product = Product(400)

    whosale = Wholesale(product)
    buyer = Buyer(product)

    product.change_price(334)
    product.change_price(285)