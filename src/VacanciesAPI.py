from abc import ABC, abstractmethod
import requests


class Parser(ABC):
    """
    Абстрактный класс для работы с API сервисов
    """

    @abstractmethod
    def get_vacancies(self, keyword):
        pass


class HeadHunterAPI(Parser):
    """
    Класс для работы с API HeadHunter
    """

    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []

    def get_vacancies(self, keyword):
        self.params['text'] = keyword
        while self.params.get('page') != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1
        return self.vacancies

class Vacancy:
    """
    Класс для работы с вакансиями
    """
    name: str
    url: str
    salary: int or str
    address: str
    experience: str

    def __init__(self, name, url, salary, address, experience):
        self.name = name
        self.url = url
        self.salary = salary
        self.address = address
        self.experience = experience

    def cast_to_object_list(self):
        pass


hh_api = HeadHunterAPI()
hh_vacancies = hh_api.get_vacancies("Python")
print(hh_vacancies)
