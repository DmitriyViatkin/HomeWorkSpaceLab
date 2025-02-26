from enum import Enum,auto
from abc import ABC, abstractmethod


class TypeCarBody(Enum):

     SEDAN = auto()
     COUPE = auto()
     CROSSOVER = auto()
     HATCHBACK = auto()
     PICKUP = auto()


class EngineType(Enum):
    Diesel = auto()
    Petrol = auto()
    Electro = auto()


class ColorBody(Enum):
    White = auto()
    Black = auto()
    Red = auto()
    Yellow = auto()
    Orange = auto()
    Green = auto()
    Blue = auto()


class Wheels(Enum):
    steel_disks = auto()
    titanium_disks = auto()


class Auto:
    def __init__(self, name):
        self.name = name
        self.body = None
        self.engine = None
        self.color = None
        self.wheels = None
        self.create_time = None

    def __str__(self):
        info: str = f"Auto name: {self.name}\n"\
                    f"Body auto {self.body} &\n"\
                    f"engine {self.engine}\n"\
                    f"color{self.color}\n"\
                    f"wheels{self.wheels}\n"\
                    f"Create time {self.create_time} days"
        return info


class Builder(ABC):

    @abstractmethod
    def create_body(self):
        pass

    @abstractmethod
    def create_engine(self):
        pass

    @abstractmethod
    def create_color_body(self):
        pass

    @abstractmethod
    def create_wheels(self):
        pass

    @abstractmethod
    def get_auto(self):
        pass


class SedanAuto (Builder):

    def __init__(self):
        self.auto = Auto("Lanos")
        self.auto.create_time = 90

    def create_body(self):
        self.auto.body = TypeCarBody.SEDAN

    def create_color_body(self):
        self.auto.color = ColorBody.Green

    def create_engine(self):
        self.auto.engine = EngineType.Petrol

    def create_wheels(self):
        self.auto.wheels = Wheels.titanium_disks

    def get_auto(self):
        return self.auto


class CoupeAuto (Builder):

    def __init__(self):
        self.auto = Auto("Запорожец")
        self.auto.create_time = 180

    def create_body(self):
        self.auto.body = TypeCarBody.COUPE

    def create_color_body(self):
        self.auto.color = ColorBody.White

    def create_engine(self):
        self.auto.engine = EngineType.Petrol

    def create_wheels(self):
        self.auto.wheels = Wheels.steel_disks

    def get_auto(self):
        return self.auto


class PICKUPAuto (Builder):

    def __init__(self):
        self.auto = Auto("L-200")
        self.auto.create_time = 190

    def create_body(self):
        self.auto.body = TypeCarBody.PICKUP

    def create_color_body(self):
        self.auto.color = ColorBody.Yellow

    def create_engine(self):
        self.auto.engine = EngineType.Diesel

    def create_wheels(self):
        self.auto.wheels = Wheels.titanium_disks

    def get_auto(self):
        return self.auto


class CROSSOVERAuto (Builder):

    def __init__(self):
        self.auto = Auto("OUTLANDER SPORT")
        self.auto.create_time = 200

    def create_body(self):
        self.auto.body = TypeCarBody.CROSSOVER

    def create_color_body(self):
        self.auto.color = ColorBody.Red

    def create_engine(self):
        self.auto.engine = EngineType.Diesel

    def create_wheels(self):
        self.auto.wheels = Wheels.titanium_disks

    def get_auto(self):
        return self.auto


List_Auto = [CROSSOVERAuto, PICKUPAuto, SedanAuto, CoupeAuto]


class Director:

    def __init__(self):
        self.builder = None

    def set_builder(self, builder: Builder):
        self.builder = builder

    def make_auto(self):
        self.builder.create_body()
        self.builder.create_engine()
        self.builder.create_color_body()
        self.builder.create_wheels()
        self.builder.get_auto()


if __name__ == "__main__":
    director = Director()
    for auto in List_Auto:
        builder = auto()
        director.set_builder(builder)
        director.make_auto()
        auto = builder.get_auto()
        print("_________________________________________________")
        print(auto)
        print("_________________________________________________")