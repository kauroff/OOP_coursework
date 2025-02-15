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

    def __init__(self) -> None:
        """
        Метод инициализации для запроса по API
        """
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []

    def get_vacancies(self, keyword) -> list:
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

    def __init__(self, name, url, salary, address, requirement, responsibility, work_format,
                 experience, employment) -> None:
        """
        Метод инициализации вакансии
        :param name: название вакансии
        :param url: ссылка на вакансию
        :param salary: уровень з/п
        :param address: город
        :param requirement: требования
        :param responsibility: обязанности
        :param work_format: формат работы
        :param experience: опыт
        :param employment: рабочий день
        """
        self.__name = name
        self.__url = f'https://hh.ru/vacancy/{url}'
        self.__salary = salary
        self.__address = address
        self.__requirement = requirement
        self.__responsibility = responsibility
        self.__work_format = work_format
        self.__experience = experience
        self.__employment = employment

    def __lt__(self, other) -> tuple:
        """
        Переопределенный метод сравнения
        :param other: другой объект класса
        :return: отсортированные вакансии
        """
        if self.salary < other.get_salary:
            return other.get_salary, self.salary

    @staticmethod
    def cast_to_object_list(list_of_vacancies: list) -> list:
        """
        Преобразование набора данных из словаря в список объектов
        :return: список объектов
        """
        vacancies_list = []
        for item in list_of_vacancies:
            if ((item['address'] is None or item['address']['city'] == 'Москва')
                    and item['experience']['name'] == 'Нет опыта'):
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
                    Vacancy(name, url, salary, address, requirement, responsibility,
                            work_format, experience, employment))
        return vacancies_list
