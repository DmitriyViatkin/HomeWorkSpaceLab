# Создаем базовый класс одиночки
class SingletonBaseClass(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonBaseClass, cls). \
                __call__(*args, **kwargs)
        return cls._instances[cls]


# создаем класс одиночку
class MySingleton(metaclass=SingletonBaseClass):
    def __init__(self):
        self.name = "Одиночка"
        self.number = '+38-066-36-367'
        self.e_mail = 'dimaviatkin@gmail.com'

    def get_contact(self):
        print("Number =" + self.name, "\n ", "e-mail = " + self.e_mail)

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name


if __name__ == "__main__":
    my_singleton_1 = MySingleton()
    my_singleton_2 = MySingleton()
    #
    print("Singleton 1: " + my_singleton_1.get_name())
    # меняем имя первому экземпляру
    my_singleton_1.set_name("John Gold")
    # выводим имена
    print("Singleton 1: " + my_singleton_1.get_name())
    print("Singleton 2: " + my_singleton_2.get_name())
    # Выводим адреса объектов
    print(my_singleton_1)
    print(my_singleton_2)
    print("Проверка по id ", id(my_singleton_1) == id(my_singleton_2))
