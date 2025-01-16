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
        Получение вакансий с hh.ru
        :param keyword: ключевое слово
        :return: Список словарей с вакансиями
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

    def __init__(self, name, url, salary, address, requirement, responsibility, work_format, experience,
                 employment):
        self.name = name
        self.url = f'https://hh.ru/vacancy/{url}'
        self.salary = salary
        self.address = address
        self.requirement = requirement
        self.responsibility = responsibility
        self.work_format = work_format
        self.experience = experience
        self.employment = employment

    @staticmethod
    def cast_to_object_list(list_of_vacancies: list):
        """
        Преобразование набора данных из словаря в список объектов
        :return: список объектов
        """
        vacancies_list = []
        for item in list_of_vacancies:
            name = item['name']
            url = item['id']
            if item['salary'] is not None:
                if item['salary']['from'] is None:
                    salary = item['salary']['to']
                else:
                    salary = item['salary']['from']
            else:
                salary = 0
            try:
                address = item['address']['city']
            except TypeError:
                address = 'Адрес не указан'
            requirement = item['snippet']['requirement']
            responsibility = item['snippet']['responsibility']
            try:
                work_format = item['work_format'][0]['name']
            except IndexError:
                work_format = 'Формат не указан'
            experience = item['experience']['name']
            employment = item['employment']['name']
            vacancies_list.append(
                Vacancy(name, url, salary, address, requirement, responsibility, work_format, experience,
                        employment))
        return vacancies_list
