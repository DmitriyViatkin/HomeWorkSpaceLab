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