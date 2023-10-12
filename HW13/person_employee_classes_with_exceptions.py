# В организации есть два типа людей: сотрудники и обычные люди. Каждый человек (и сотрудник, и обычный) имеет
# следующие атрибуты:
# Фамилия (строка, не пустая) Имя (строка, не пустая) Отчество (строка, не пустая) Возраст (целое положительное число)
# Сотрудники имеют также уникальный идентиф.номер (ID), который должен быть шестизначным положительным целым числом.
# Ваша задача:
#   Создать класс Person, который будет иметь атрибуты и методы для управления данными о людях
# (Фамилия, Имя, Отчество, Возраст). Класс должен проверять валидность входных данных и генерировать исключения
# InvalidNameError и InvalidAgeError, если данные неверные.
#   Создать класс Employee, который будет наследовать класс Person и добавлять уникальный идентификационный номер (ID).
# Класс Employee также должен проверять валидность ID и генерировать исключение InvalidIdError, если ID неверный.
#   Добавить метод birthday в класс Person, который будет увеличивать возраст человека на 1 год.
#   Добавить метод get_level в класс Employee, который будет возвращать уровень сотрудника на основе суммы цифр
# в его ID (по остатку от деления на 7).
#   Создать несколько объектов класса Person и Employee с разными данными и проверить, что исключения работают корректно
# при передаче неверных данных.

class Person:
    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int):
        if not isinstance(last_name, str) or last_name == '':
            raise InvalidNameError(last_name)
        self.last_name = last_name
        if not isinstance(first_name, str) or first_name == '':
            raise InvalidNameError(first_name)
        self.first_name = first_name
        if not isinstance(patronymic, str) or patronymic == '':
            raise InvalidNameError(patronymic)
        self.patronymic = patronymic
        if not isinstance(age, int) or age <= 0:
            raise InvalidAgeError(age)
        self._age = age

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}, возраст: {self.age} лет'

    def birthday(self):
        return self._age + 1

    def get_age(self):
        return self._age


class Employee(Person):
    list_id = []

    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int, emp_id: int):
        Person.__init__(self, last_name, first_name, patronymic, age)
        if isinstance(emp_id, int) and emp_id in range(100_000, 1_000_000):
            if emp_id not in self.__class__.list_id:
                self.emp_id = emp_id
                self.__class__.list_id.append(self.emp_id)
            else:
                raise NonUniqueIDError(emp_id)
        else:
            raise InvalidIdError(emp_id)

    def get_level(self):
        digits_sum = 0
        lvl = int(self.emp_id)
        while lvl:
            digits_sum += lvl % 10
            lvl //= 10
        return digits_sum % 7 + 1


class OwnBaseError(Exception):
    def __init__(self, message: str):
        self.message = message

    def __str__(self):
        return self.message


class InvalidNameError(OwnBaseError):
    def __init__(self, name: str):
        super(InvalidNameError, self).__init__(f'Invalid name: {name}. Name should be a non-empty string.')


class InvalidAgeError(OwnBaseError):
    def __init__(self, value: int):
        super(InvalidAgeError, self).__init__(f'Invalid age: {value}. Age should be a positive integer.')


class InvalidIdError(OwnBaseError):
    def __init__(self, value: int):
        super(InvalidIdError, self).__init__(f'Invalid id: {value}. '
                                             f'Id should be a 6-digit positive integer between 100000 and 999999.')


class NonUniqueIDError(OwnBaseError):
    def __init__(self, value: int):
        super(NonUniqueIDError, self).__init__(f'Invalid ID: {value}. Such ID already exists.')


# # pers = Person('Виталий', 'Крюк', 'Андреевич', 45)
# # print(pers.birthday())
# pers2 = Employee('Крюк', 'Виталий', 'Андреевич', 45, '963584')
# print(pers2.get_level())
# print(pers2)
# pers3 = Employee('Ковалев', 'Дмитрий', 'Николаевич', 20, '113113')
# print(pers3.get_level())
# print(pers3)
# print(pers3.birthday())
# # pers4 = Employee('Мурашко', 'Ирина', 'Викторовна', 32, '113113')
# # print(pers4.get_level())
# # print(pers4)

employee = Employee("Bob", "Johnson", "Brown", 40, 12345)
# Ожидаемый ответ:
#
# __main__.InvalidIdError: Invalid id: 12345. Id should be a 6-digit positive integer between 100000 and 999999.
#
# Ваш ответ:
#
# AttributeError: 'int' object has no attribute 'isdigit'

person = Person("Alice", "Smith", "Johnson", 25)
print(person.get_age())
# Ожидаемый ответ
# 25
#
# Ошибка:
#
# Traceback (most recent call last):
#   File "5HXQ4NKRCVALK2L9LDYR.py", line 81, in <module>
#     print(person.get_age())
# AttributeError: 'Person' object has no attribute 'get_age'
