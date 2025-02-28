class Kitchen:
    def preparing_food(self):
        print("Готовим вам еду")

    def give_away_food(self):
        print("Еда готова")


class Barista:
    def preparing_coffee(self):
        print("Ваш Coffee готовится ")

    def give_away_coffee(self):
        print("Coffe готов")




class User:
    def __init__(self, name):
        self.name = name

    def set_order(self):

        print(f"{self.name}  Мне кофе и еды")

    def get_name(self):
        return self.name

    def pay_order(self):
        print("Оплачу картой")

class Waiter:
    def __init__(self):
        self.barista = Barista()
        self.kichen = Kitchen()

    def get_ordef(self, client: User):
        print(f"{client.get_name()} , ваш заказ готовится  ")
        self.barista.preparing_coffee()
        self.kichen.preparing_food()

    def give_away_order(self):
        self.barista.give_away_coffee()
        self.kichen.give_away_food()

    def check(self):
        print("Ваш счет за кофе и еду")


if __name__ == "__main__":

    waiter = Waiter()
    client = User('Bob')
    client.set_order()
    waiter.get_ordef(client)
    waiter.give_away_order()
    waiter.check()
    client.pay_order()

