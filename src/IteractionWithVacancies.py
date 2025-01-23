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

    @staticmethod
    def __valid(vacancies_list: list):
        """
        Метод для валидации данных
        :param vacancies_list: список объектов вакансий
        :return: список словарей вакансий
        """
        data = []

        for vacancy in vacancies_list:
            if (vacancy.__address == ('Москва' or 'Адрес не указан') and
                    (vacancy.__experience == 'Нет опыта') and
                    (vacancy.__salary is int and not None) and ((vacancy.__name,
                                                               vacancy.__url,
                                                               vacancy.__requirement,
                                                               vacancy.__responsibility,
                                                               vacancy.__work_format,
                                                               vacancy.__employment) is str and not None)):
                data.append({'name': vacancy.__name,
                             'url': vacancy.__url,
                             'salary': vacancy.__salary,
                             'address': vacancy.__address,
                             'requirement': vacancy.__requirement,
                             'responsibility': vacancy.__responsibility,
                             'work_format': vacancy.__work_format,
                             'experience': vacancy.__experience,
                             'employment': vacancy.__employment})
        return data

    def add_info(self, vacancies_list: list):
        """
        Метод для записи вакансий в JSON-файл с валидацией данных
        :param vacancies_list: список объектов вакансий
        """
        data = {'vacancies': []}

        data['vacancies'].extend(JSONSaver.__valid(vacancies_list))

        with open(f'{self.__filename}.json', "w+", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False)

    def delete_info(self):
        """
        Метод для удаления данных из файла
        """
        data = ''
        with open(f'{self.__filename}.json', "w+", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False)

    def add_vacancy(self, vacancy):
        """
        Метод для добавления вакансии в файл
        :param vacancy: объект класса вакансии
        """
        with open(f'{self.__filename}.json', 'r', encoding='utf-8') as file:
            vacancies_data = json.load(file)

        vacancies_data['vacancies'].append(JSONSaver.__valid([vacancy]))

        with open(f'{self.__filename}.json', 'w', encoding='utf-8') as file:
            json.dump(vacancies_data, file, ensure_ascii=False)

    def get_vacancy(self, parameter):
        """
        Метод для получения вакансии по заданному параметру
        :param parameter: заданный параметр
        :return: вакансия или ответ об ее отсутствии
        """
        with open(f'{self.__filename}.json', 'r', encoding='utf-8') as file:
            vacancies_data = json.load(file)

        for uniq_vacancy in vacancies_data['vacancies']:
            if parameter in uniq_vacancy.values():
                name = uniq_vacancy['name']
                url = uniq_vacancy['url']
                salary = uniq_vacancy['salary']
                address = uniq_vacancy['address']
                requirement = uniq_vacancy['requirement']
                responsibility = uniq_vacancy['responsibility']
                work_format = uniq_vacancy['work_format']
                experience = uniq_vacancy['experience']
                employment = uniq_vacancy['employment']
                return f"""\n
                Вот, что удалось найти:\n
                {name}\n
                {url}\n
                {salary}\n
                {address}\n
                {requirement}\n
                {responsibility}\n
                {work_format}\n
                {experience}\n
                {employment}\n
                """
            else:
                return 'Вакансии с таким значением нет'

    def delete_vacancy(self, url):
        """
        Метод для удаления вакансии из файла
        :param url: параметр для поиска вакансии в файле
        :return: сообщение об окончании
        """
        with open(f'{self.__filename}.json', 'r', encoding='utf-8') as file:
            vacancies_data = json.load(file)

        flag = False
        for uniq_vacancy in vacancies_data['vacancies']:
            if url == uniq_vacancy['url']:
                vacancies_data['vacancies'].remove(uniq_vacancy)
                flag = True

        with open(f'{self.__filename}.json', 'w+', encoding='utf-8') as file:
            json.dump(vacancies_data, file, ensure_ascii=False)

        if flag:
            return 'Вакансия успешно удалена'
        else:
            return 'Вакансии с таким url нет'


class ExcelSaver(Connector):
    def add_vacancy(self, vacancy):
        pass

    def get_vacancy(self, **kwargs):
        pass

    def delete_vacancy(self, **kwargs):
        pass
