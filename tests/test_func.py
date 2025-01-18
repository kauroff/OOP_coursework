import pytest
from src.func import filter_vacancies, get_vacancies_by_salary, sort_vacancies, get_top_vacancies, print_vacancies


@pytest.fixture
filtered = filter_vacancies([{
    "name": "",
    "url": "",
    "salary": 100000,
    "address": "Москва",
    "requirement": "word",
    "responsibility": "",
    "work_format": "",
    "experience": "",
    "employment": ""
},
    {
        "name": "",
        "url": "",
        "salary": 60000,
        "address": "Адрес не указан",
        "requirement": None,
        "responsibility": "",
        "work_format": "",
        "experience": "",
        "employment": ""
    },
    {
        "name": "",
        "url": "",
        "salary": 50000,
        "address": "Адрес не указан",
        "requirement": "",
        "responsibility": "word",
        "work_format": "",
        "experience": "",
        "employment": ""
    }], ['word'])


def test_filter_vacancies():
    assert filtered == [{
        "name": "",
        "url": "",
        "salary": 100000,
        "address": "Москва",
        "requirement": "word",
        "responsibility": "",
        "work_format": "",
        "experience": "",
        "employment": ""
    },
    {
        "name": "",
        "url": "",
        "salary": 50000,
        "address": "Адрес не указан",
        "requirement": "",
        "responsibility": "word",
        "work_format": "",
        "experience": "",
        "employment": ""
    }]
