import pytest
from src.IteractionWithVacancies import JSONSaver
from src.VacanciesAPI import Vacancy


@pytest.fixture
def saver():
    saver = JSONSaver()
    vacancy_1 = Vacancy("a", "b", 100000, "Москва", "word", "c", "d", 'Нет опыта', "e")
    vacancy_2 = Vacancy("", "", 60000, "Адрес не указан", None, "", "", 'Нет опыта', "")
    saver.add_info([vacancy_1, vacancy_2])
    return saver


def test_get_info(saver):
    assert saver.get_info() == {'vacancies': [
        {'name': 'a', 'url': 'https://hh.ru/vacancy/b', 'salary': 100000, 'address': 'Москва', 'requirement': 'word',
         'responsibility': 'c',
         'work_format': 'd', 'experience': 'Нет опыта', 'employment': 'e'},
        {'name': '', 'url': 'https://hh.ru/vacancy/', 'salary': 60000, 'address': 'Адрес не указан',
         'requirement': None, 'responsibility': '',
         'work_format': '', 'experience': 'Нет опыта', 'employment': ''}]}


def test_add_info(saver):
    vacancy_0 = Vacancy("a", "b", 100000, "Москва", "word", "c", "d", 'Нет опыта', "e")
    saver.add_info([vacancy_0])
    assert saver.get_info() == {'vacancies': [
        {'name': 'a', 'url': 'https://hh.ru/vacancy/b', 'salary': 100000, 'address': 'Москва',
         'requirement': 'word',
         'responsibility': 'c',
         'work_format': 'd', 'experience': 'Нет опыта', 'employment': 'e'}]}


def test_delete_info(saver):
    saver.delete_info()
    assert saver.get_info() == ''


def test_add_vacancy(saver):
    saver.add_vacancy(Vacancy('a', 'a', 10, 'a', 'a', 'a', 'a', 'a', 'a'))
    assert saver.get_info() == {'vacancies': [
        {'name': 'a', 'url': 'https://hh.ru/vacancy/b', 'salary': 100000, 'address': 'Москва', 'requirement': 'word',
         'responsibility': 'c',
         'work_format': 'd', 'experience': 'Нет опыта', 'employment': 'e'},
        {'name': '', 'url': 'https://hh.ru/vacancy/', 'salary': 60000, 'address': 'Адрес не указан',
         'requirement': None, 'responsibility': '',
         'work_format': '', 'experience': 'Нет опыта', 'employment': ''},
        {'name': 'a', 'url': 'https://hh.ru/vacancy/a', 'salary': 10, 'address': 'a', 'requirement': 'a',
         'responsibility': 'a',
         'work_format': 'a', 'experience': 'a', 'employment': 'a'}]}


def test_get_vacancy(saver):
    assert saver.get_vacancy('') == 'Вакансии с таким значением нет'


def test_delete_vacancy(saver):
    assert saver.delete_vacancy('') == 'Вакансии с таким url нет'
