def filter_vacancies(vacancies_list: list, filter_words: list):
    """
    Функция, которая отбирает только подходящие по описанию вакансии
    :param vacancies_list: список объектов класса вакансий
    :param filter_words: слова для фильтрации
    :return: список объектов подходящих вакансий
    """
    data = []
    for item in vacancies_list:
        try:
            requirement = item.get_requirement.split()
        except AttributeError:
            requirement = []
        try:
            responsibility = item.get_responsibility.split()
        except AttributeError:
            responsibility = []

        for word in filter_words:
            if (word in (requirement + responsibility)) and (item not in data):
                data.append(item)
    return data


def get_vacancies_by_salary(filtered_vacancies: list, salary_range: int):
    """
    Функция, которая отбирает только подходящие по зарплате вакансии (и в т.ч. если зп не указана)
    :param filtered_vacancies: список объектов подходящих вакансий
    :param salary_range: желаемая зарплата
    :return: список объектов подходящих вакансий
    """
    data = []
    for item in filtered_vacancies:
        if salary_range < item.get_salary:
            data.append(item)
    return data


def sort_vacancies(ranged_vacancies: list):
    """
    Функция, которая сортирует подходящие вакансии по заработной плате
    :param ranged_vacancies: список объектов подходящих вакансий
    :return: отсортированный список объектов
    """
    N = len(ranged_vacancies)
    for i in range(N):
        for j in range(N - 1 - i):
            if ranged_vacancies[j] < ranged_vacancies[j + 1]:
                continue
    return ranged_vacancies


def get_top_vacancies(sorted_vacancies: list, top_n: int):
    """
    Функция, которая показывает топ-н вакансий по заработной плате
    :param sorted_vacancies: отсортированный список объектов
    :param top_n: количество вакансий
    :return: конечный результат
    """
    return sorted_vacancies[:top_n]


def show_vacancies(top_vacancies: list):
    """
    Функция, которая выводит результат в консоль
    :param top_vacancies: конечный результат
    :return: None
    """
    for element in top_vacancies:
        return f'''\n{element.get_name}
        \n{element.get_url}
        \n{element.get_salary}
        \n{element.get_address}
        \n{element.get_requirement}
        \n{element.get_responsibility}
        \n{element.get_work_format}
        \n{element.get_experience}
        \n{element.get_employment}
        \n________________________________'''
