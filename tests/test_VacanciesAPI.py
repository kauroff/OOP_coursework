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
    assert vacancy.name == 'a'
    assert vacancy.url == 'https://hh.ru/vacancy/b'
    assert vacancy.salary == 100000
    assert vacancy.address == 'Москва'
    assert vacancy.requirement == 'word'
    assert vacancy.responsibility == 'c'
    assert vacancy.work_format == 'd'
    assert vacancy.experience == 'Нет опыта'
    assert vacancy.employment == 'e'


# def test_cast_to_object_list(vacancy):
#     assert vacancy.cast_to_object_list([{'name': 'a', 'id': 'a', 'salary': None, 'address': {'city': 'a'},
#                                          'snippet': {'requirement': 'a', 'responsibility': 'a'}, 'work_format': [
#             {'name': 'a'}], 'experience': {'name': 'a'}, 'employment': {'name': 'a'}}]) == [vacancy]
