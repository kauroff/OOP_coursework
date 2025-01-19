import pytest
from src.IteractionWithVacancies import JSONSaver
from src.VacanciesAPI import Vacancy


@pytest.fixture
def saver():
    vacancy_1 = Vacancy("a", "b", 100000, "Москва", "word", "c", "d", 'Нет опыта', "e")
    vacancy_2 = Vacancy("", "", 60000, "Адрес не указан", None, "", "", 'Нет опыта', "")
    return JSONSaver([vacancy_1, vacancy_2])


def test_init(saver):
    assert len(saver.vacancies_list) == 2


# def test_init(saver):
#     assert JSONSaver(saver).vacancies_list == saver

def test_add_vacancy(saver):
    vacancy_1 = Vacancy("a", "b", 100000, "Москва", "word", "c", "d", 'Нет опыта', "e")
    assert saver.add_vacancy(vacancy_1) is None


def test_get_vacancy(saver):
    assert saver.get_vacancy('') is None


def test_delete_vacancy(saver):
    assert saver.delete_vacancy('') is None
