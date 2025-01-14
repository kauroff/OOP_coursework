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
        """
        Получение вакансий с hh.ru в формате JSON
        :param keyword: ключевое слово
        :return: JSON-словарь с вакансиями
        """
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

    def __init__(self, name, url, salary, vacancy_type, address, requirement, responsibility, work_format, experience,
                 employment):
        self.name = name
        self.url = f'https://hh.ru/vacancy/{url}'
        self.salary = salary
        self.vacancy_type = vacancy_type
        self.address = address
        self.requirement = requirement
        self.responsibility = responsibility
        self.work_format = work_format
        self.experience = experience
        self.employment = employment

    @staticmethod
    def cast_to_object_list(list_of_vacancies: list):
        """
        Преобразование набора данных из JSON в список объектов
        :return: список объектов
        """
        vacancies_list = []
        for item in list_of_vacancies:
            name = item['name']
            url = item['id']
            salary = item['salary']
            vacancy_type = item['type']
            try:
                address = item['address']['city']
            except:
                address = None
            requirement = item['snippet']['requirement']
            responsibility = item['snippet']['responsibility']
            try:
                work_format = item['work_format'][0]['name']
            except:
                work_format = None
            experience = item['experience']['name']
            employment = item['employment']['name']
            vacancies_list.append(
                Vacancy(name, url, salary, vacancy_type, address, requirement, responsibility, work_format, experience,
                        employment))
        return vacancies_list


hh_api = HeadHunterAPI()
hh_vacancies = hh_api.get_vacancies("Python")
# print(hh_vacancies)
print(Vacancy.cast_to_object_list(hh_vacancies))
