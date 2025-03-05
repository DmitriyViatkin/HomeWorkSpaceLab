from abc import  ABC, abstractmethod


class Reader(ABC):
    @abstractmethod
    def parser(self, url:str):
        pass

class ResourceReader:
    def __init__(self, reader: Reader):
        self.__reader = reader

    def set_strategy(self, reader: Reader):
        self.__reader = reader
    def read(self, url: str):
        self.__reader.parser(url)


class NewsSiteReader(Reader):
    def parser(self, url:str):
        print("Parsing news Site ", url)


class SocialNetworkReader(Reader):
    def parser(self, url:str):
        print("Parsing SocialNetwork ", url)


if __name__ == "__main__":

    resource_reader  = ResourceReader(NewsSiteReader())
    url = 'https://news.ua'
    resource_reader.read(url)
    url = "https://facebook.com"
    resource_reader.set_strategy(SocialNetworkReader())
    resource_reader.read(url)