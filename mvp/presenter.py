from messageStore import MessageStore
from view import  View


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


