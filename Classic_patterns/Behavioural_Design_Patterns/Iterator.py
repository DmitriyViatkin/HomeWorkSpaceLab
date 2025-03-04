from abc import ABC, abstractmethod


class Iterator(ABC):
    @abstractmethod
    def next(self):
        pass

    @abstractmethod
    def has_next(self):
        pass


class BookDictionaryIterator(Iterator):


    def __init__(self, books):
        self._books = list(books.items())  # Преобразуем словарь в список пар (ключ, значение)
        self._index = 0

    def next(self):
        try:
            book = self._books[self._index]
            self._index += 1
            return book
        except IndexError:
            return None

    def has_next(self):
        return self._index < len(self._books)


class BookIterator(Iterator):
    def __init__(self,books):
        self._books = books
        self._index = 0

    def next(self):
        try:
            book = self._books[self._index]
            self._index += 1
            return book
        except IndexError:
            return None

    def has_next(self):
        return self._index < len(self._books)


class BookCollection:

    def __init__(self, books = None, _books_dict = None):
        self._books = books or []
        self._books_dict = None or {}
    def add_book(self, books):
        self._books.append(books)

    def add_book_dict(self, title, author):

        self._books_dict[title] = author

    def create_interator_list(self):
        return BookIterator(self._books)

    def create_interator_dict(self):
        return BookDictionaryIterator(self._books_dict)


if __name__ == "__main__":
    Library = ["Программирование на Python в примерах и задачах", "Изучаем Python: программирование игр, визуализация данных, веб-приложения", "Простой Python. Современный стиль программирования, 2-е издание"]
    library = BookCollection(Library)
    library_1 = BookCollection()
    library.add_book("Мастер и Маргарита")
    library.add_book("Преступление и наказание")
    library.add_book("Война и мир")
    library_1.add_book_dict("Мастер и Маргарита", "Булгаков")
    library_1.add_book_dict("Преступление и наказание" , "Достоевский")
    library_1.add_book_dict("Война и мир", "Толстой")




    iterator_list = library.create_interator_list()
    iterator_dict = library_1.create_interator_dict()
    while iterator_list.has_next():
        book = iterator_list.next()
        print(book)
    print("#"*15)

    while iterator_dict.has_next():
        book = iterator_dict.next()
        print(book)