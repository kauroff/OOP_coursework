from abc import ABC, abstractmethod
import json


class Connector(ABC):
    """
    Абстрактный класс, который обязывает реализовать методы
    """

    @abstractmethod
    def add_vacancy(self, vacancy):
        """
        Добавление вакансии
        :param vacancy: обект класса
        :return: None
        """
        pass

    @abstractmethod
    def get_vacancy(self, **kwargs):
        """
        Получение вакансии из файла по указанным критериям
        :param kwargs: необходимые критерии
        :return: Список вакансий
        """
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        """
        Удаление информации о вакансии.
        :param вакансию для удаления
        :return: None
        """
        pass


class JSONSaver(Connector):
    """
    Сохранение информации о вакансиях в JSON-файл
    """

    def __init__(self, vacancies_list):
        self.vacancies_list = vacancies_list
        with open('data/vacancies.json', 'r', encoding='utf-8') as file:
            data = json.load(file, ensure_ascii=False, indent=4)

        with open('..data/vacancies.json', 'w', encoding='utf-8') as file:
            json.dump(self.vacancies_list, file, ensure_ascii=False, indent=4)

    def add_vacancy(self, vacancy):
        pass

    def get_vacancy(self, **kwargs):
        pass

    def delete_vacancy(self, vacancy):
        pass


class ExcelSaver(Connector):
    def add_vacancy(self, vacancy):
        pass

    def get_vacancy(self, **kwargs):
        pass

    def delete_vacancy(self, **kwargs):
        pass


with open('C:/Users/crazy/PycharmProjects/OOP_coursework/data/vacancies.json', 'r', encoding='utf-8') as file:
    data = json.loads(file, ensure_ascii=False, indent=4)
print(data)