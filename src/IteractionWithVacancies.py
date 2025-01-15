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
        """
        Метод инициализации для записи вакансий в JSON-файл
        :param vacancies_list: список вакансий
        """
        self.vacancies_list = vacancies_list
        data = {'vacancies': []}

        for vacancy in vacancies_list:
            data['vacancies'].append({'name': vacancy.name,
                                      'url': f'https://hh.ru/vacancy/{vacancy.url}',
                                      'salary': vacancy.salary,
                                      'address': vacancy.address,
                                      'requirement': vacancy.requirement,
                                      'responsibility': vacancy.responsibility,
                                      'work_format': vacancy.work_format,
                                      'experience': vacancy.experience,
                                      'employment': vacancy.employment})

        with open("vacancies.json", "w+", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def add_vacancy(self, vacancy):

        new_vacancy = {'name': vacancy.name,
                       'url': f'https://hh.ru/vacancy/{vacancy.url}',
                       'salary': vacancy.salary,
                       'address': vacancy.address,
                       'requirement': vacancy.requirement,
                       'responsibility': vacancy.responsibility,
                       'work_format': vacancy.work_format,
                       'experience': vacancy.experience,
                       'employment': vacancy.employment}

        with open('data/vacancies.json', 'r', encoding='utf-8') as file:
            vacancies_data = json.load(file, ensure_ascii=False, indent=4)

        new_data = vacancies_data['vacancies'].append(new_vacancy)

        with open('data/vacancies.json', 'w+', encoding='utf-8') as file:
            json.dump(new_data, file, ensure_ascii=False, indent=4)

    def get_vacancy(self, **kwargs):
        with open('data/vacancies.json', 'r+', encoding='utf-8') as file:
            vacancies_data = json.load(file, ensure_ascii=False, indent=4)

        for uniq_vacancy in vacancies_data['vacancies']:
            if kwargs.values() in uniq_vacancy.values():
                return uniq_vacancy

    def delete_vacancy(self, url):
        with open('data/vacancies.json', 'r+', encoding='utf-8') as file:
            vacancies_data = json.load(file, ensure_ascii=False, indent=4)

        for uniq_vacancy in vacancies_data['vacancies']:
            if uniq_vacancy['url'] == url:
                del uniq_vacancy

        with open('data/vacancies.json', 'w+', encoding='utf-8') as file:
            json.dump(vacancies_data, file, ensure_ascii=False, indent=4)


class ExcelSaver(Connector):
    def add_vacancy(self, vacancy):
        pass

    def get_vacancy(self, **kwargs):
        pass

    def delete_vacancy(self, **kwargs):
        pass
