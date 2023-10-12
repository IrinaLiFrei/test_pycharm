# 📌 На семинаре 13 был создан проект по работе с пользователями (имя, id, уровень)
# 📌 Напишите 3-7 тестов pytest (или unittest на ваш выбор) для данного проекта
# 📌 ОБЯЗАТЕЛЬНО! Используйте фикстуры

import pytest
from access_data_by_STONE import *
from access_data_by_STONE_descriptors import *


@pytest.fixture
def get_company():
    return Company('Coca-Cola')

@pytest.fixture
def remove_file():
    file = 'Coca-Cola.json'
    yield file
    os.remove(file)

@pytest.fixture
def employee_1():
    employee_1 = Employee('Some Good Man', 5, '349583')
    return employee_1


@pytest.fixture
def employee_2():
    employee_2 = Employee('Some Good Man', 5, '349583')
    return employee_2


@pytest.fixture
def employee_3():
    employee_3 = Employee('Another Good Man', 5, '545524')
    return employee_3


def test_hiring_success(get_company, employee_1):
    get_company.hiring(employee_1, 'Successfully Hired Man', '869558', 3)
    assert True


def test_hiring_level_error(get_company, employee_1):
    with pytest.raises(LevelError):
        get_company.hiring(employee_1, 'Not Good Man', '645285', 7)


def test_hiring_id_error(get_company, employee_1):
    with pytest.raises(UniqueID):
        get_company.hiring(employee_1, 'SameID Hired Man', '869558', 4)


def test_login_true(get_company, employee_1):
    get_company.login('Successfully Hired Man', '869558')
    assert True


def test_login_error(get_company, employee_1, employee_3, remove_file):
    with pytest.raises(AccessError):
        get_company.login(employee_1.name, employee_3.employee_id)


if __name__ == '__main__':
    pytest.main(['-v'])

