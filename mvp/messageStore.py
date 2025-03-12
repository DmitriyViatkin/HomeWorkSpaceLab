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