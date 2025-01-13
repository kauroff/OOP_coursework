from abc import ABC, abstractmethod


class Connector(ABC):
    pass


class JSONSaver(Connector):
    def add_vacancy(self, vacancy):
        pass

    def delete_vacancy(self, vacancy):
        pass
