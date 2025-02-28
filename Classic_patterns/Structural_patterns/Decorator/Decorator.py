class Book:
    def __init__(self, name):
        self.name = name

    def open(self):
        print(f"you open book  '{self.name}'")

    def close (self):
        print(f"you close book  '{self.name}'")


class DecoratorBook(Book):
    def read(self):
        print(f"you read book  '{self.name}'")


book = DecoratorBook("Expansion")
book.open()
book.read()
book.close()