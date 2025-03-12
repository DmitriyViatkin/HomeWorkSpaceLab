class View:
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