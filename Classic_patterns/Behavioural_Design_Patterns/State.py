from abc import ABC, abstractmethod


class State(ABC):
    def __init__(self):
        self._state_doc: 'StateDoc' = None

    @abstractmethod
    def next_state(self):
        pass

    @abstractmethod
    def previous_state(self):
        pass


class StateDoc:
    def __init__(self, st:State):
        self.set_state(st)

    def set_state(self, st: State):
        self.__state = st
        self.__state._state_doc = self

    def next_state(self):
        self.__state.next_state()

    def previous_state(self):
        self.__state.previous_state()


class StateDraft(State):
    def next_state(self):
        print("Draft")
        self._state_doc.set_state(StateModeration())

    def previous_state(self):
        print("Draft")


class StateModeration(State):
    def next_state(self):
        print("Moderation")
        self._state_doc.set_state(StatePublished())

    def previous_state(self):
        print("Draft")


class StatePublished(State):
    def next_state(self):
        print("Published")


    def previous_state(self):
        print("Draft")
        self._state_doc.set_state(StateModeration())


if __name__ == "__main__":

    document = StateDoc(StateDraft())
    document.next_state()
    document.next_state()
    document.next_state()
    document.next_state()
    document.previous_state()
    document.next_state()
    document.next_state()