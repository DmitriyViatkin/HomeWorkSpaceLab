from abc import ABC, abstractmethod
from typing import List


class Imemento(ABC):
    @abstractmethod
    def get_dollars(self):
        pass

    @abstractmethod
    def get_euro(self):
        pass


class ExchangeMemento(Imemento):
    def __init__(self, dollars, euro):
        self.__dollars = dollars
        self.__euro = euro
    def get_dollars(self):
        return self.__dollars

    def get_euro(self):
        return self.__euro


class Exchange:
    def __init__(self, dollars, euro):
        self.__dollars = dollars
        self.__euro = euro

    def get_dollars(self):
        print(f"dollars{self.__dollars}")

    def get_euro(self):
        print(f"euro{self.__euro}")

    def sell_dollars(self):
        if self.__dollars >0:
            self.__dollars-=1

    def sell_euro(self):
        if self.__euro >0:
            self.__euro-=1

    def buy_dollars(self):
        self.__dollars +=1

    def buy_euro(self):
        self.__euro +=1

    def save(self):
        return ExchangeMemento(self.__dollars, self.__euro)
    def restore(self,exchange_memento: Imemento):
        self.__dollars = exchange_memento.get_dollars()
        self.__euro = exchange_memento.get_euro()


class Memory:

    def __init__(self, exchange: Exchange):
        self.__exchange = exchange
        self.__history : List[Imemento] =[]

    def bakup(self):
        self.__history.append(self.__exchange.save())

    def  undo (self):
        if len(self.__history) == 0:
            return
        else:
            self.__exchange.restore(self.__history.pop())

if __name__ == "__main__":

    exchange = Exchange(10, 10)
    memory = Memory(exchange)

    exchange.get_dollars()
    exchange.get_euro()
    print()
    print("Save" * 20)
    print()
    memory.bakup()
    print( )
    print("Sall"*20)
    print()
    exchange.sell_dollars()
    exchange.buy_euro()
    exchange.get_dollars()
    exchange.get_euro()
    print()
    print("Save" * 20)
    print()
    #exchange.save()
    print()
    print("Sall" * 20)
    print()
    exchange.sell_dollars()
    exchange.buy_euro()
    exchange.get_dollars()
    exchange.get_euro()
    print()
    print("Restore" * 20)
    print()
    memory.undo()
    exchange.get_dollars()
    exchange.get_euro()

