from typing import Dict, List


class Shared:
    def __init__(self, company, position):
        self.__company = company
        self.__position = position

    def get_company(self):
        return self.__company

    def get_position(self):
        return self.__position


class Unique:
    def __init__(self, name, surname):
        self.__name = name
        self.__surname = surname

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname


class Flyweight:
    def __init__(self, shared: Shared, ):
        self.__shared = shared
        #self.__human = human

    def process(self, human: Unique):
        print(f"{self.__shared.get_company()} {self.__shared.get_position()}")
        print(f"{human.get_name()} {human.get_surname()}")


    def get_data(self):
        return self.__shared.get_company() + '  ' + self.__shared.get_position()


class FlyweightFactory:
    def get_key(self, shared: Shared):

        return f'{shared.get_company()} + " and "+ {shared.get_position()}'

    def __init__(self, shareds: list[Shared]):
        self.__flyweights: Dict[str, Flyweight] = {}
        for shared in shareds:
            self.__flyweights[self.get_key(shared)] = Flyweight(shared)

    def get_flyweight(self, shared: Shared):
        key = self.get_key(shared)
        if self.__flyweights.get(key) is None:
            self.__flyweights[key] = Flyweight(shared)
        else:
            return self.__flyweights[key]
        return self.__flyweights[key]

    def list_flyweights(self):
        count = len(self.__flyweights)
        print(count)
        for pair in self.__flyweights.values():
            print(pair.get_data())


class Specialist_database:

    def add_specialist_database(ff: FlyweightFactory,company, position, name, surname):
        print("add specialist")
        flyweight = ff.get_flyweight(Shared(company, position))
        flyweight.process(Unique(name, surname))

class Proxy(Specialist_database):
    def __init__(self, real_subject):
        self.human = []
        self.__real_subject = real_subject

    def add_specialist_database(self,ff: FlyweightFactory,
                                company, position, name, surname):

        flyweight = ff.get_flyweight(Shared(company, position))
        flyweight.process(Unique(name, surname))
        unique = Unique(name, surname)
        flyweight.process(unique)
        self.human.append(unique)

    def get_human(self):
        print("Список людей:")
        for h in self.human:
            print(f"{h.get_name()} {h.get_surname()}")


if __name__ == '__main__':
    data = Specialist_database()
    proxy = Proxy(data)
    shared_list: List[Shared] = [Shared("TNK", "SEO"),
                                 Shared("UMC", "HR")]
    factory = FlyweightFactory(shared_list)
    factory.list_flyweights()
    proxy.add_specialist_database(factory, "ЗЖРК", "Электро механик", "John", "Gold")
    proxy.add_specialist_database(factory, "ЗЖРК", "Электро механик", "Igor", "Gold")
    proxy.add_specialist_database(factory, "ЗЖРК", "мастер", "Igor", "Gold")
    factory.list_flyweights()
    proxy.get_human()
