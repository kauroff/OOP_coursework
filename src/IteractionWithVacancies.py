from abc import ABC, abstractmethod
import json


class Connector(ABC):
    """
    Абстрактный класс, который обязывает реализовать методы
    """

    @abstractmethod
    def add_vacancy(self, vacancy) -> None:
        """
        Метод для добавления вакансии в файл
        :param vacancy: объект класса вакансии
        """
        pass

    @abstractmethod
    def get_vacancy(self, parameter) -> None:
        """
        Получение вакансии из файла по указанным критериям
        :param parameter: необходимый критерий
        :return: Список вакансий
        """
        pass

    @abstractmethod
    def delete_vacancy(self, url) -> str:
        """
        Метод для удаления вакансии из файла
        :param url: параметр для поиска вакансии в файле
        :return: сообщение об окончании
        """
        pass

    @abstractmethod
    def get_info(self) -> dict:
        """
        Метод для получения данных из файла
        :return: JSON-словарь со всеми вакансиями
        """
        pass

    @abstractmethod
    def add_info(self, vacancies_list) -> None:
        """
        Метод для записи вакансий в JSON-файл с валидацией данных
        :param vacancies_list: список объектов вакансий
        """
        pass

    @abstractmethod
    def delete_info(self) -> None:
        """
        Метод для удаления данных из файла
        """
        pass


class JSONSaver(Connector):
    """
    Сохранение информации о вакансиях в JSON-файл
    """

    def __init__(self, filename='vacancies') -> None:
        """
        Метод инициализации для записи вакансий в JSON-файл
        :param filename: название файла
        """
        self.__filename = f'{filename}.json'

    def get_info(self) -> dict:
        """
        Метод для получения данных из файла
        :return: JSON-словарь со всеми вакансиями
        """
        with open(self.__filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data

    def add_info(self, vacancies_list: list) -> None:
        """
        Метод для записи вакансий в JSON-файл с валидацией данных
        :param vacancies_list: список объектов вакансий
        """
        data = {'vacancies': []}

        for vacancy in vacancies_list:
            data['vacancies'].append({'name': vacancy.name,
                                      'url': vacancy.url,
                                      'salary': vacancy.salary,
                                      'address': vacancy.address,
                                      'requirement': vacancy.requirement,
                                      'responsibility': vacancy.responsibility,
                                      'work_format': vacancy.work_format,
                                      'experience': vacancy.experience,
                                      'employment': vacancy.employment})

        with open(self.__filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False)

    def delete_info(self) -> None:
        """
        Метод для удаления данных из файла
        """
        data = ''
        with open(self.__filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False)

    def add_vacancy(self, vacancy) -> None:
        """
        Метод для добавления вакансии в файл
        :param vacancy: объект класса вакансии
        """
        with open(self.__filename, 'r', encoding='utf-8') as file:
            vacancies_data = json.load(file)

        vacancies_data['vacancies'].append({'name': vacancy.name, 'url': vacancy.url,
                                            'salary': vacancy.salary, 'address': vacancy.address,
                                            'requirement': vacancy.requirement,
                                            'responsibility': vacancy.responsibility,
                                            'work_format': vacancy.work_format,
                                            'experience': vacancy.experience,
                                            'employment': vacancy.employment})

        with open(self.__filename, 'w', encoding='utf-8') as file:
            json.dump(vacancies_data, file, ensure_ascii=False)

    def get_vacancy(self, parameter) -> str:
        """
        Метод для получения вакансии из файла по заданному параметру
        :param parameter: заданный параметр
        :return: вакансия или ответ об ее отсутствии
        """
        with open(self.__filename, 'r', encoding='utf-8') as file:
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
                return f"""
                {name}
                {url}
                {salary}
                {address}
                {requirement}
                {responsibility}
                {work_format}
                {experience}
                {employment}
                """
            else:
                return 'Вакансии с таким значением нет')

    def delete_vacancy(self, url) -> str:
        """
        Метод для удаления вакансии из файла
        :param url: параметр для поиска вакансии в файле
        :return: сообщение об окончании
        """
        with open(self.__filename, 'r', encoding='utf-8') as file:
            vacancies_data = json.load(file)

        flag = False
        for uniq_vacancy in vacancies_data['vacancies']:
            if url == uniq_vacancy['url']:
                vacancies_data['vacancies'].remove(uniq_vacancy)
                flag = True

        with open(self.__filename, 'w+', encoding='utf-8') as file:
            json.dump(vacancies_data, file, ensure_ascii=False)

        if flag:
            return 'Вакансия успешно удалена'
        else:
            return 'Вакансии с таким url нет'
