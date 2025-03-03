from abc import ABC, abstractmethod


class Handlers_1(ABC):

    @abstractmethod
    def set_next(self, handler: "Handlers_1"):
        pass

    @abstractmethod
    def handle(self, request):
        pass


class AbstractHandler(Handlers_1):

    _next_handler: Handlers_1 = None

    def set_next(self, handler: Handlers_1):
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request):

        if self._next_handler:
            return self._next_handler.handle(request)
        return None


class Carpenter(AbstractHandler):
    def handle(self, request):
        if request == "tree":
            return "Я работаю с деревом. \n Делаю мебель "
        else:
            return super().handle(request)


class Mechanic(AbstractHandler):
    def handle(self, request):
        if request == "car":
            return "Я чиню машины"
        else:
            return super().handle(request)


class Electrician(AbstractHandler):
    def handle(self, request):
        if request == "light":
            return "Я работаю с электро приборами"
        else:
            return super().handle(request)

def client_cod(handler: Handlers_1):

    for prob in ['tree','light','car','bicycle']:
        result = handler.handle(prob)
        if result:
            print(result)
        else:
            print("sorry")
if __name__ == "__main__":
    tree = Carpenter()
    light = Electrician()
    car = Mechanic()
    tree.set_next(tree).set_next(car)

    client_cod(tree)
