from src.VacanciesAPI import HeadHunterAPI, Vacancy
from src.IteractionWithVacancies import JSONSaver
from src.func import filter_vacancies, get_top_vacancies, sort_vacancies, get_vacancies_by_salary, print_vacancies

hh_api = HeadHunterAPI()


# Функция для взаимодействия с пользователем
def user_interaction():
    # platforms = ["HeadHunter"]
    search_query = input("Введите поисковый запрос: ")
    hh_vacancies = hh_api.get_vacancies(search_query)
    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)
    json_saver = JSONSaver(vacancies_list)
    answer = input('''Если хотите добавить вакансию в файл - введите A
    \nЕсли хотите удалить вакансию из файла - введите D
    \nЕсли хотите продолжить работать с программой без изменений - нажмите enter''')
    if answer == 'A':
        name, url, salary, address, requirement, responsibility, work_format, experience, employment = input(
            '''Введите вакансию для добавления в файл в формате: <Название вакансии>, <Ссылка на вакансию>, <Зарплата>, 
            <Адрес>, <Требования>, <Обязанности>, <Формат работы>, <Опыт>, <График>
            \nЕсли не хотите добавлять - нажмите enter''').split(', ')
        vacancy = Vacancy(name, url, salary, address, requirement, responsibility, work_format, experience, employment)
        json_saver.add_vacancy(vacancy)
    elif answer == 'D':
        try:
            url = input('Введите url вакансии в формате <https://hh.ru/vacancy/123456>')
            json_saver.delete_vacancy(url)
        except ValueError:
            print('Вакансии с таким url нет')

    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_range = input("Введите желаемую зарплату: ")  # Пример: 100000

    filtered_vacancies = filter_vacancies(vacancies_list, filter_words)

    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)

    sorted_vacancies = sort_vacancies(ranged_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print_vacancies(top_vacancies)


if __name__ == "__main__":
    user_interaction()
