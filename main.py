from src.VacanciesAPI import HeadHunterAPI, Vacancy
from src.IteractionWithVacancies import JSONSaver
from src.func import filter_vacancies, get_top_vacancies, sort_vacancies, get_vacancies_by_salary, print_vacancies

hh_api = HeadHunterAPI()


# Функция для взаимодействия с пользователем
def user_interaction() -> None:
    search_query = input("Введите поисковый запрос: ").lower()
    hh_vacancies = hh_api.get_vacancies(search_query)
    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)
    json_saver = JSONSaver()
    json_saver.add_info(vacancies_list)
    answer = input('''Если хотите добавить вакансию в файл - введите A
    \nЕсли хотите получить вакансию из файла по указанному критерию - введите G
    \nЕсли хотите удалить вакансию из файла - введите D
    \nЕсли хотите продолжить работать с программой без изменений - нажмите enter\nВвод: ''')

    if answer == 'A':
        name, url, salary, address, requirement, responsibility, work_format, experience, employment = input(
            '''Введите вакансию для добавления в файл в формате: <Название вакансии>, <Ссылка на вакансию>, <Зарплата>,
            <Адрес>, <Требования>, <Обязанности>, <Формат работы>, <Опыт>, <График>:\n''').split(', ')
        try:
            vacancy = Vacancy(name, url, salary, address, requirement, responsibility, work_format,
                              experience, employment)
            json_saver.add_vacancy(vacancy)
        except ValueError:
            print('Неподходящий тип данных')
    elif answer == 'G':
        parameter = input('Введите значение: ')
        json_saver.get_vacancy(parameter)
    elif answer == 'D':
        url = input('Введите url вакансии в формате <https://hh.ru/vacancy/123456>: ')
        json_saver.delete_vacancy(url)
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_range = int(input("Введите желаемую зарплату: "))
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))

    filtered_vacancies = filter_vacancies(vacancies_list, filter_words)

    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)

    sorted_vacancies = sort_vacancies(ranged_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print_vacancies(top_vacancies)


if __name__ == "__main__":
    user_interaction()
