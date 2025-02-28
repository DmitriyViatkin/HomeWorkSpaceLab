from abc import ABC, abstractmethod


class Product(ABC):
    @abstractmethod
    def cost(self):
        pass

    @abstractmethod
    def name(self):
        pass


class RProduct(Product):

    def __init__(self, name, cost):
        self._name = name
        self._cost = cost

    def cost(self):
        return self._cost

    def name(self):
        return self._name


class CompoundProduct(Product):
    def __init__(self, name):
        self._name = name
        self.products = []

    def cost(self):
        cost = 0
        for it in self.products:
            cost += it.cost()
        return cost

    def name(self):
        return self._name

    def add_product(self, product: Product):
        self.products.append(product)

    def remove_product(self, product: Product):
        self.products.remove(product)

    def cler(self):
        self.products = []


class Bag(CompoundProduct):
    """Класс пиццы"""
    def __init__(self, name: str):
        super(Bag, self).__init__(name)

    def cost(self):
        cost = 0
        for it in self.products:
            cost_it = it.cost()
            print(f"Стоимость '{it.name()}' = {cost_it} тугриков")
            cost += cost_it
        print(f"Стоимость товара '{self.name()}' = {cost} тугриков")
        return cost


if __name__ == "__main__":

    vegetables = CompoundProduct("vegetables")
    vegetables.add_product(RProduct("cucumbers", 3))
    vegetables.add_product(RProduct("tomato", 2.3))
    vegetables.add_product(RProduct("salat", 1))
    vegetables.add_product(RProduct("cabbage", 2.1))
    oil = RProduct("Oil", 12.1)
    fruits = CompoundProduct("fruits")
    fruits.add_product(RProduct("orange", 14))
    fruits.add_product(RProduct("Kivi", 12.3))
    fruits.add_product(RProduct("banana", 9.54))

    bag = Bag("purchase")
    bag.add_product(vegetables)
    bag.add_product(oil)
    bag.add_product(fruits)
    print(bag.cost())
