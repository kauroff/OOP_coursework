from abc import ABC, abstractmethod


class Vacancy:
    def __init__(self, name: str, url: str, salary: str, desc: str, experience: str):
        self.name = name
        self.url = url
        self.salary = salary
        self.desc = desc
        self.experience = experience

    def cast_to_object_list(self):
        pass


class JSONSaver:
    def add_vacancy(self, vacancy):
        pass

    def delete_vacancy(self, vacancy):
        pass
