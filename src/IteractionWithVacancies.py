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
        :param vacancy: объект класса
        :return: None
        """
        pass

    @abstractmethod
    def get_vacancy(self, parameter):
        """
        Получение вакансии из файла по указанным критериям
        :param parameter: необходимый критерий
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

    def __init__(self, filename='vacancies'):
        """
        Метод инициализации для записи вакансий в JSON-файл
        :param filename: название файла
        """
        self.__filename = filename

    def get_info(self):
        """
        Метод для получения данных из файла
        :return: JSON-словарь со всеми вакансиями
        """
        with open(f'{self.__filename}.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data

    def add_info(self, vacancies_list):
        """
        Метод для записи вакансий в JSON-файл
        :param vacancies_list: список вакансий
        """
        data = {'vacancies': []}

        for vacancy in vacancies_list:
            if vacancy.address == ('Москва' or 'Адрес не указан') and vacancy.experience == 'Нет опыта':
                data['vacancies'].append({'name': vacancy.name,
                                          'url': vacancy.url,
                                          'salary': vacancy.salary,
                                          'address': vacancy.address,
                                          'requirement': vacancy.requirement,
                                          'responsibility': vacancy.responsibility,
                                          'work_format': vacancy.work_format,
                                          'experience': vacancy.experience,
                                          'employment': vacancy.employment})

        with open(f'{self.__filename}.json', "w+", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False)

    def delete_info(self):
        """
        Метод для удаления данных из файла
        :return: None
        """
        data = ''
        with open(f'{self.__filename}.json', "w+", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False)

    def add_vacancy(self, vacancy):

        new_vacancy = {'name': vacancy.name,
                       'url': vacancy.url,
                       'salary': vacancy.salary,
                       'address': vacancy.address,
                       'requirement': vacancy.requirement,
                       'responsibility': vacancy.responsibility,
                       'work_format': vacancy.work_format,
                       'experience': vacancy.experience,
                       'employment': vacancy.employment}

        with open(f'{self.__filename}.json', 'r', encoding='utf-8') as file:
            vacancies_data = json.load(file)

        vacancies_data['vacancies'].append(new_vacancy)

        with open(f'{self.__filename}.json', 'w', encoding='utf-8') as file:
            json.dump(vacancies_data, file, ensure_ascii=False)

    def get_vacancy(self, parameter):
        with open(f'{self.__filename}.json', 'r', encoding='utf-8') as file:
            vacancies_data = json.load(file)

        for uniq_vacancy in vacancies_data['vacancies']:
            if parameter in uniq_vacancy.values():
                print()
                print('Вот, что удалось найти:')
                print(uniq_vacancy['name'])
                print(uniq_vacancy['url'])
                print(uniq_vacancy['salary'])
                print(uniq_vacancy['address'])
                print(uniq_vacancy['requirement'])
                print(uniq_vacancy['responsibility'])
                print(uniq_vacancy['work_format'])
                print(uniq_vacancy['experience'])
                print(uniq_vacancy['employment'])
                print()
            else:
                print('Вакансии с таким значением нет')

    def delete_vacancy(self, url):
        with open(f'{self.__filename}.json', 'r', encoding='utf-8') as file:
            vacancies_data = json.load(file)

        flag = False
        for uniq_vacancy in vacancies_data['vacancies']:
            if url == uniq_vacancy['url']:
                vacancies_data['vacancies'].remove(uniq_vacancy)
                print('Вакансия успешно удалена')
                flag = True
        if not flag:
            print('Вакансии с таким url нет')

        with open(f'{self.__filename}.json', 'w+', encoding='utf-8') as file:
            json.dump(vacancies_data, file, ensure_ascii=False)


class ExcelSaver(Connector):
    def add_vacancy(self, vacancy):
        pass

    def get_vacancy(self, **kwargs):
        pass

    def delete_vacancy(self, **kwargs):
        pass
