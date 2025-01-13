from abc import ABC, abstractmethod


class Vacancy():
    def __init__(self, name: str, url: str, salary: str, experience: str):
        self.name = name
        self.url = url
        self.salary = salary
        self.experience = experience
    def cast_to_object_list(self):
        pass


class JSONSaver(ABC):
    pass
