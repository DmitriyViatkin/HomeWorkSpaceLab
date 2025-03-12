class View:
    def set_presenter(self, presenter):
        self.presenter = presenter


    def show_messages(self,message):
        if not message:
            print("Сообщений пока нет")
        else:
            for mess in message:
                for i, k in mess.items():
                    print(f"{i}: {k}")
    def show_message(self,message):
        if not message:
            print("Сообщений пока нет")
        else:
             for i, k in message.items():
                    print(f"{i}: {k}")

    def show_text(self,text):
        print(text)

    def run(self):

         while True:
             print(
                    "\n1. Добавить сообщение\
                    \n2. Показать все сообщения\
                    \n3. Показать сообщения автора\
                    \n4. Показать сообщение по номеру\
                     \n5. Удалить сообщение \
                     \n6. Удалить автора \
                     \n7. Выйти")
             command = int(input("Сделай свой вибор"))

             if command == 1:
                 self.presenter.add_message(input("Кто автор"), input("Введите Ваше сообщение"))

             elif command == 2:
                 self.presenter.show_all_messages()

             elif command == 3:

                 self.presenter.show_message_author(input("Введите автора"))

             elif command == 4:
                 self.presenter.show_message_id(int(input("Введите номер сообщения")))

             elif command == 5:
                 self.presenter.del_message_id(int(input("Введите номер сообщения")))

             elif command == 6:
                 self.presenter.del_message_author(input("Введите автора"))

             elif command == 7:
                 break
import json
from pyexpat.errors import messages

class MessageStore:
    def __init__(self, filename='message.json'):
        self.file = filename
    def add_message(self, author, message):
        data = self.load_data()

        mess= {
            "id": int(self.get_id()),
            "author": author,
            "message": message
        }

        data.append(mess)

        self.write(data)

    def write(self,data):

        with open(self.file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def get_all_message(self):

        return self.load_data()

    def get_message_id(self,id):
        for i in  self.load_data():
            if i['id'] == id:
                return i

    def get_message_author(self,author):
        for i in  self.load_data():
            if i['author'] == author:
                return i

    def load_data(self):
        try:
            with open(self.file, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []
        return data

    def get_id(self):
        max_id = 0
        data = self.load_data()
        if data:
            for i in data:
                try:
                    current_id = int(i['id'])
                    if current_id > max_id:
                        max_id = current_id
                except (KeyError, ValueError):
                    pass
        return max_id + 1

    def del_id(self,id):
        mess = self.load_data()
        data_new = []
        for i in mess:
            if i['id'] != id:
               data_new.append(i)
        self.write(data_new)

    def del_author(self,author):
        mess = self.load_data()
        data_new = []
        for i in mess:
            if i['author'] != author:
               data_new.append(i)
        self.write(data_new)

class Presenter:
    def __init__(self):
                self.model = MessageStore()
                self.view = View()

    def add_message(self, author, text):
        self.model.add_message(author, text)
        self.view.show_text("Сообщение добавленно")

    def show_all_messages(self):
        messages = self.model.get_all_message()
        self.view.show_messages(messages)

    def show_message_id(self, id):
        messages = self.model.get_message_id(id)
        self.view.show_message(messages)

    def show_message_author(self, author):
        messages = self.model.get_message_author(author)
        self.view.show_message(messages)

    def del_message_id(self, mess_id):
        self.model.del_id(mess_id)
        self.view.show_text("Сообщение удаленно")

    def del_message_author(self, mess_author):
        self.model.del_id(mess_author)
        self.view.show_text("Автора удаленно")




if __name__ == "__main__":
    view=View()
    presenter = Presenter()
    view.set_presenter(presenter)
    view.run()

