from pyexpat.errors import messages

from view import View
from model import  MessageStore

class Controller:
    def __init__(self):
        self.model= MessageStore()
        self.view = View()

    def add_message(self, author, text):
        self.model.add_message(author, text)
        self.view.show_text("Сообщение добавленно")

    def show_all_messages(self):
        messages = self.model.get_all_message()
        self.view.show_messages(messages)

    def show_message_id (self, id):
        messages= self.model.get_message_id(id)
        self.view.show_message(messages)

    def show_message_author (self, author):
        messages= self.model.get_message_author(author)
        self.view.show_message(messages)

    def del_message_id (self, mess_id):
        self.model.del_id(mess_id)
        self.view.show_text("Сообщение удаленно")

    def del_message_author (self, mess_author):
        self.model.del_id(mess_author)
        self.view.show_text("Автора удаленно")

    def run(self):

        while True:
            print(
                "\n1. Добавить сообщение\n2. Показать все сообщения\
                \n3. Показать сообщения автора\n4. Показать сообщение по номеру\
                  \n5. Удалить сообщение \n6. Удалить автора \n7. Выйти")

            command= int(input("Сделай свой вибор"))

            if command == 1:
                messages.add_message(input("Кто автор"),input("Введите Ваше сообщение"))

            elif command ==  2 :
                messages.show_all_messages()

            elif command ==  3 :

                messages.show_message_author(input("Введите автора"))

            elif command ==  4 :
                messages.show_message_id(int(input("Введите номер сообщения")))

            elif command == 5:
                messages.del_message_id(int(input("Введите номер сообщения")))

            elif command == 6:
                messages.del_message_author(input("Введите автора"))

            elif command == 7 :
                break










if  __name__ == "__main__":
    messages = Controller()
    messages.run()
