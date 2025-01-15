def filter_vacancies(vacancies_list, filter_words):
    """
    Функция, которая отбирает только подходящие по описанию вакансии
    :param vacancies_list: список объектов класса вакансий
    :param filter_words: слова для фильтрации
    :return: список объектов подходящих вакансий
    """
    data = []
    for item in vacancies_list:
        try:
            requirement = item.requirement.split()
        except AttributeError:
            requirement = []
        try:
            responsibility = item.responsibility.split()
        except AttributeError:
            responsibility = []

        if (filter_words in (requirement and responsibility) and item.experience == 'Нет опыта' or 'От 1 года до 3 лет'
                and item.address == 'Москва'):
            data.append(item)

    return data


def get_vacancies_by_salary(filtered_vacancies, salary_range):
    """
    Функция, которая отбирает только подходящие по зарплате вакансии (и в т.ч. если зп не указана)
    :param filtered_vacancies: список объектов подходящих вакансий
    :param salary_range: желаемая зарплата
    :return: список объектов подходящих вакансий
    """
    data = []
    for item in filtered_vacancies:
        if int(salary_range) < item.salary:
            data.append(item)
    return data


def sort_vacancies(ranged_vacancies):
    """
    Функция, которая сортирует подходящие вакансии по заработной плате
    :param ranged_vacancies: список объектов подходящих вакансий
    :return: отсортированный список объектов
    """
    N = len(ranged_vacancies)
    for i in range(N):
        for j in range(N - 1 - i):
            if ranged_vacancies[j].salary < ranged_vacancies[j + 1].salary:
                ranged_vacancies[j].salary, ranged_vacancies[j + 1].salary = ranged_vacancies[j + 1].salary, \
                    ranged_vacancies[j].salary
    return ranged_vacancies


def get_top_vacancies(sorted_vacancies, top_n):
    """
    Функция, которая показывает топ-н вакансий по заработной плате
    :param sorted_vacancies: отсортированный список объектов
    :param top_n: количество вакансий
    :return: конечный результат
    """
    return sorted_vacancies[:top_n]


def print_vacancies(top_vacancies):
    """
    Функция, которая выводит результат в консоль
    :param top_vacancies: конечный результат
    :return: конечный результат
    """
    for element in top_vacancies:
        print(element)
