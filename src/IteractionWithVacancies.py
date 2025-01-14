from abc import ABC, abstractmethod


class Connector(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancy(self, **kwargs):
        pass

    @abstractmethod
    def delete_vacancy(self, **kwargs):
        pass


class JSONSaver(Connector):
    def add_vacancy(self, vacancy):
        pass

    def get_vacancy(self, **kwargs):
        pass

    def delete_vacancy(self, **kwargs):
        pass
