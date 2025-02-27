from abc import ABC, abstractmethod

"""
Класс пробега авто в милях
"""


class Odomer(ABC):
    def __init__(self):
        self.start = None
        self.finish = None

    @abstractmethod
    def get_mill(self):
        pass

    @abstractmethod
    def set_milli(self, start, finish):
        pass


class OdometerC(ABC):
    @abstractmethod
    def get_mill(self):
        pass

    @abstractmethod
    def set_kilometer(self):
        pass

    def get_kilometer(self):
        pass


class OdometerUSA(Odomer):
    def __init__(self):
        super().__init__()

    def get_mill(self):
        return self.finish - self.start

    def set_milli(self, start, finish):
        self.start = start
        self.finish = finish


class AdapterKilometer(OdometerC):
    MILL = 1.609

    def __init__(self, mills: OdometerUSA):
        self.mill = mills

    def get_mill(self):
        return self.mill.get_mill()

    def set_kilometer(self, start, finish):
        start = start / AdapterKilometer.MILL
        finish = finish / AdapterKilometer.MILL
        return self.mill.set_milli(start, finish)

    def get_kilometer(self):
        return self.get_mill() * AdapterKilometer.MILL


drivs = OdometerUSA()
"""drivs.set_milli(200, 300)
print(drivs.get_mill())"""

driv = AdapterKilometer(drivs)
driv.set_kilometer(100, 300)
print("Milli", drivs.get_mill())

print("Kilometer", driv.get_kilometer())
