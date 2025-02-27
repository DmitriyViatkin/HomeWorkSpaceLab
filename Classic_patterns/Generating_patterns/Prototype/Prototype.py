from abc import ABC, abstractmethod
import copy
from Classic_patterns.Generating_patterns.builder_car.builder_car import (TypeCarBody, EngineType, ColorBody, Wheels)


class IPrototype(ABC):
    @abstractmethod
    def clone(self):
        pass


class Auto(IPrototype):

    def __init__(self, name="Unknown",
                 body=TypeCarBody.SEDAN,
                 engine=EngineType.Petrol,
                 color=ColorBody.Yellow,
                 wheels=Wheels.titanium_disks,
                 create_time=160):
        self.name = name
        self.body = body
        self.engine = engine
        self.color = color
        self.wheels = wheels
        self.create_time = create_time

    def __str__(self):
        info: str = f"Auto name: {self.name}\n" \
                    f"Body auto {self.body} &\n" \
                    f"engine {self.engine}\n" \
                    f"color{self.color}\n" \
                    f"wheels{self.wheels}\n" \
                    f"Create time {self.create_time} days"
        return info

    def clone(self):
        return type(self)(
            name=self.name,
            body=self.body,
            engine=self.engine,
            color=self.color,
            wheels=self.wheels,
            create_time=self.create_time
        )


if __name__ == "__main__":
    auto = Auto("F")
    new_auto = auto.clone()
    print("__________________________________")
    print(auto)
    new_auto.name = "Fortuna"
    print("__________________________________")

    green_lanos = copy.deepcopy(new_auto)
    green_lanos.name = "Sonata"
    green_lanos.color = ColorBody.Green
    print(green_lanos)
    print("__________________________________")