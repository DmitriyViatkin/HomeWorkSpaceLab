from abc import ABC, abstractmethod


class Contact(ABC):
    @abstractmethod
    def print_contact(self, name, surname, phone):
        pass


class Contact_1(Contact):
    def print_contact(self, name, surname, phone):
        print(f" Name:{name} \n Surname: {surname} \n Phone:{phone}")


class Contact_2(Contact):
    def print_contact(self, name, surname, phone):
        print("________________________")
        print(f" FirstName:  {name} ")
        print("________________________")
        print(f" Surname:  {surname} ")
        print("________________________")
        print(f" Phone number:  {phone}")
        print("________________________")


class Human(ABC):

    @abstractmethod
    def change_contact(self, name, surname, phone):
        pass


class Client(Human):
    def __init__(self, name, surname, phone, contact):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.print_con = contact

    def change_contact(self, name, surname, phone):
        self.name = name
        self.surname = surname
        self.phone = phone

    def print_contakt(self):
        self.print_con.print_contact(self.name, self.surname, self.phone)


if __name__ == "__main__":

    boy = Client("dima", "Viatkin", 88888888, Contact_1())

    boy.print_contakt()
    print("_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_")
    boy_2 = Client("Vlad", "Drozdov", 966638998, Contact_2())
    boy_2.print_contakt()