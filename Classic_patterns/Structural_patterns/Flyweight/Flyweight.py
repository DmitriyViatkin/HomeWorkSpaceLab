from typing import  Dict, List


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
    def __init__(self, shared: Shared):
        self.__shared = shared

    def process(self, unique: Unique):
        print(f"{self.__shared.get_company()}_{self.__shared.get_position()}")

    def get_data(self):
        return self.__shared.get_company() + '__' +self.__shared.get_position()


class FlyweightFactory:
    def get_key(self, shared: Shared):

        return f'{shared.get_company()} + " and "+ {shared.get_position()}'

    def __init__(self, shareds: list[Shared]):
        self.__flyweights: Dict[str, Flyweight] = {}
        for shared in shareds:
            self.__flyweights[self.get_key(shared)]=Flyweight(shared)

    def get_flyweight(self, shared:Shared):
        key=self.get_key(shared)
        if self.__flyweights.get(key) is  None:
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
    def add_specialist_database(ff:FlyweightFactory, company, position, name, surname):
        print("add")
        flyweight = ff.get_flyweight(Shared(company, position))
        flyweight.process(Unique(name, surname))


if __name__ == '__main__':
    shared_list: List[Shared] = [Shared("TNK", "SEO"),
        Shared("UMC", "HR")]
    factory = FlyweightFactory(shared_list)
    factory.list_flyweights()
    Specialist_database.add_specialist_database(factory, "ЗЖРК", "Электро мехвник", "John", "Gold")
    factory.list_flyweights()