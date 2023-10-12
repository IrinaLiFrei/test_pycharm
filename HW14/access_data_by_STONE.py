# Доработаем задачи 3 и 4. Создайте класс проекта, который имеет следующие методы:
# загрузка данных (функция из задания 4)
# -- вход в систему - требует указать имя и id пользователя. Для проверки наличия пользователя в множестве используйте
# магический метод проверки на равенство пользователей.
# Если такого пользователя нет, вызывайте исключение доступа. А если пользователь есть, получите его уровень из
# множества пользователей.
# -- добавление пользователя. Если уровень пользователя меньше, чем ваш уровень, вызывайте исключение уровня доступа.

from faker import Faker
import random
import json
import os
from access_data_by_STONE_descriptors import *


def create_employee(company: str, count: int):
    employees = {}
    list_id = []
    for _ in range(count):
        name = Faker('ru_RU').name()
        while True:
            employee_id = str(random.randint(1, 999999)).zfill(6)
            if employee_id not in list_id:
                list_id.append(employee_id)
                break
        lvl_access = int(employee_id) % 7 + 1
        if lvl_access in employees:
            employees[lvl_access][employee_id] = name
        else:
            employees[lvl_access] = {employee_id: name}
    with open(f'{company}.json', 'w', encoding='UTf-8') as file:
        json.dump(employees, file, indent=4, ensure_ascii=False)
    return employees



class Employee:
    name = EmployeeName()
    employee_id = EmployeeID()

    def __init__(self, name: str, lvl_access: int, employee_id: str):
        self.name = name
        self.lvl_access = lvl_access
        self.employee_id = employee_id
        if 0 < int(lvl_access) < 8:
            self.lvl_access = int(lvl_access)
        else:
            raise ValueError

    def __str__(self):
        return f'{self.name} ({self.employee_id}) | Access level: {self.lvl_access}'

    def __eq__(self, other):
        return self.name == other.name and self.employee_id == other.employee_id



class Company:
    def __init__(self, name: str):
        self.name = name
        if os.path.exists(f'{self.name}.json'):
            with open(f'{self.name}.json', 'r', encoding='UTF-8') as file:
                employees_list = json.load(file)
        else:
            employees_list = create_employee(self.name, 10)
        self.employees = [Employee(e_name, e_lvl, e_id)
                          for e_lvl, person in employees_list.items()
                          for e_id, e_name in person.items()]

# nike = Company('NIKE')
# print(*nike.employees, sep='\n')

    def login(self, name: str, e_id: str):
        for employee in self.employees:
            if employee.name == name and employee.employee_id == e_id:
                return employee
        raise AccessError(Employee(name, 1, e_id))

    def hiring(self, me: Employee, new_name: str, new_id: str, new_lvl: int):
        if me:
            if me.lvl_access > new_lvl:
                if new_id not in [employee.employee_id for employee in self.employees]:
                    self.employees.append(Employee(new_name, int(new_lvl), new_id))
                    self.__save()
                    print(f'{new_name} was successfully hired')
                else:
                    raise UniqueID(new_id)
            else:
                raise LevelError(me, Employee(new_name, new_lvl, new_id))

        else:
            raise AccessError(me)

    def __save(self):
        employees_list = {}
        for employee in self.employees:
            if employee.lvl_access in employees_list:
                employees_list[employee.lvl_access][employee.employee_id] = employee.name
            else:
                employees_list[employee.lvl_access] = {employee.employee_id: employee.name}
        with open(f'{self.name}.json', 'w', encoding='UTF-8') as file:
            json.dump(employees_list, file, indent=4, ensure_ascii=False)


# nike = Company('NIKE')
# print(*nike.employees, sep='\n')
# print('============================')
# me = nike.login('Клавдия Оскаровна Калинина', '383730')
# nike.hiring(me, 'Пушкин Александр Сергеевич', '968968', 4)


