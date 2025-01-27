import pytest
from src.VacanciesAPI import HeadHunterAPI, Vacancy


@pytest.fixture
def parser():
    hh = HeadHunterAPI()
    return hh


def test_init_parser(parser):
    assert parser.url == 'https://api.hh.ru/vacancies'
    assert parser.headers == {'User-Agent': 'HH-User-Agent'}
    assert parser.params == {'text': '', 'page': 0, 'per_page': 100}
    assert parser.vacancies == []


def test_get_vacancies(parser):
    assert parser.get_vacancies('saodhoashdioasd') == []


@pytest.fixture
def vacancy():
    vacancy = Vacancy("a", "b", 100000, "Москва", "word", "c", "d", 'Нет опыта', "e")
    return vacancy


def test_init_vacancy(vacancy):
    assert vacancy.get_name == 'a'
    assert vacancy.get_url == 'https://hh.ru/vacancy/b'
    assert vacancy.get_salary == 100000
    assert vacancy.get_address == 'Москва'
    assert vacancy.get_requirement == 'word'
    assert vacancy.get_responsibility == 'c'
    assert vacancy.get_work_format == 'd'
    assert vacancy.get_experience == 'Нет опыта'
    assert vacancy.get_employment == 'e'
