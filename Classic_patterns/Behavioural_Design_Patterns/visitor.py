from abc import ABC, abstractmethod
from typing import List


class IVisitor(ABC):
    @abstractmethod
    def visit(self, place: "IPlace"):
        pass


class IPlace(ABC):
    @abstractmethod
    def accept(self,visitor:IVisitor):
        pass


class Zoo(IPlace):
    def accept(self,visitor:IVisitor):
        visitor.visit(self)


class Shop(IPlace):
    def accept(self,visitor:IVisitor):
        visitor.visit(self)


class Cinema(IPlace):
    def accept(self,visitor:IVisitor):
        visitor.visit(self)


class Circus(IPlace):
    def accept(self,visitor:IVisitor):
        visitor.visit(self)


class Visitor(IVisitor):
    def __init__(self):
        self.value = ''

    def visit(self, place: "IPlace"):
        if isinstance(place,Zoo):
            self.value = 'I see Monkey'
        elif isinstance(place, Cinema):
            self.value = "I see Matrix"
        elif isinstance(place, Shop):
            self.value = "I see Product"
        elif isinstance(place, Circus):
            self.value = "I see Clown"


if __name__ == "__main__" :

    places: List [IPlace] = [Zoo(),Circus(),Cinema(),Shop()]
    for place in places:
        visitor = Visitor()
        place.accept(visitor)
        print(visitor.value)
