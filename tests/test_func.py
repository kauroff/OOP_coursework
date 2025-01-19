import pytest
from src.func import filter_vacancies, get_vacancies_by_salary, sort_vacancies, get_top_vacancies, print_vacancies
from src.VacanciesAPI import Vacancy


@pytest.fixture
def filtered():
    vacancy_1 = Vacancy("a", "b", 100000, "Москва", "word", "c", "d", 'Нет опыта', "e")
    vacancy_2 = Vacancy("", "", 60000, "Адрес не указан", None, "", "", 'Нет опыта', "")
    vacancy_3 = Vacancy("", "", 50000, "Адрес не указан", "word", "", "", 'Нет опыта', "")
    return [vacancy_1, vacancy_2, vacancy_3]


def test_filter_vacancies(filtered):
    assert filter_vacancies(filtered, ['word']) == [filtered[0], filtered[2]]


def test_get_vacancy_by_salary(filtered):
    assert get_vacancies_by_salary(filtered, 55000) == [filtered[0], filtered[1]]


def test_sort_vacancies(filtered):
    assert sort_vacancies(filtered) == [filtered[0], filtered[1], filtered[2]]


def test_get_top_vacancies(filtered):
    assert get_top_vacancies(filtered, 2) == [filtered[0], filtered[1]]


def test_print_vacancies(filtered):
    assert print_vacancies(filtered) is None
