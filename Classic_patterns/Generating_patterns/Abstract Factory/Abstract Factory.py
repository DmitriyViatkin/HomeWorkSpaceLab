from abc import ABC, abstractmethod

"""
Базовые классы продуктов
"""


class Car(ABC):
    def __init__(self, car):
        self._car = car

    @abstractmethod
    def create(self):
        pass


class Bicycle(ABC):
    def __init__(self, bicycle):
        self._bicycle = bicycle

    @abstractmethod
    def create(self):
        pass


class Motorbike(ABC):
    def __init__(self, motorbike):
        self._motorbike = motorbike

    @abstractmethod
    def create(self):
        pass


"""
Производные классы транспорта марки Ауди
"""


class AudiCar(Car):
    def __init__(self):
        super().__init__("Audi")

    def create(self):
        print(f'Created car {self._car}')


class AudiBicycle(Bicycle):
    def __init__(self):
        super().__init__("Audi")

    def create(self):
        print(f'Created bicycle {self._bicycle}')


class AudiMotorbike(Motorbike):
    def __init__(self):
        super().__init__("Audi")

    def create(self):
        print(f'Created bicycle {self._motorbike}')


"""
Производные классы транспорта марки Mazda
"""


class MazdaCar(Car):
    def __init__(self):
        super().__init__("Mazda")

    def create(self):
        print(f'Created car {self._car}')


class MazdaBicycle(Bicycle):
    def __init__(self):
        super().__init__("Mazda")

    def create(self):
        print(f'Created bicycle {self._bicycle}')


class MazdaMotorbike(Motorbike):
    def __init__(self):
        super().__init__("Audi")

    def create(self):
        print(f'Created bicycle {self._motorbike}')


"""
Базовый класс абстрактной фабрики
"""


class TransportAbstractFactory(ABC):
    @abstractmethod
    def get_Car(self):
        pass

    @abstractmethod
    def getBicycle(self):
        pass

    @abstractmethod
    def getMotorbike(self):
        pass


"""
Производные классы абстрактной фабрики,
конкретные реализации для каждой из марки
"""


class AudiFactory(TransportAbstractFactory):
    def get_Car(self):
        return AudiCar()

    def getBicycle(self):
        return AudiBicycle()

    def getMotorbike(self):
        return AudiMotorbike()


class MazdaFactory(TransportAbstractFactory):
    def get_Car(self):
        return MazdaCar()

    def getBicycle(self):
        return MazdaBicycle()

    def getMotorbike(self):
        return MazdaMotorbike()


"""
Пользовательский код
"""


class ShopTransport:
    def __init__(self, factory: TransportAbstractFactory):
        self._factory = factory

    def create_tr(self):
        my_car = self._factory.get_Car()
        my_bicycle = self._factory.getBicycle()
        my_motorbike = self._factory.getMotorbike()

        my_car.create()
        my_bicycle.create()
        my_motorbike.create()

    def create_factory(transport):  # функция создающая необходимую фабрику
        factory = {
            "Audi": AudiFactory,
            "Mazda": MazdaFactory
        }
        return factory[transport]()


if __name__ == '__main__':
    brend = "Audi"
    transport = ShopTransport.create_factory(brend)
    product = ShopTransport(transport)
    product.create_tr()
