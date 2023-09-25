# Напишите следующие функции:
# Нахождение корней квадратного уравнения
# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
# Соберите пакет с играми из тех файлов, что уже были созданы в рамках курса
import csv
import json
import random
from functools import wraps
from math import sqrt
from typing import Callable


def json_deco(path: str):
    def deco(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            data = {}
            result = func(*args, **kwargs)
            data[str(*args) + str(*kwargs)] = result
            with open(path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            return data
        return wrapper
    return deco


def csv_reading_deco(path: str):
    def deco(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = {}
            with open(path, 'r', encoding='utf-8') as f:
                csv_file = csv.reader(f)
                for line in csv_file:
                    elms = [list(map(int, s.split())) for s in line]
                    for el in elms:
                        a, b, c = el[0], el[1], el[2]
                        result[str(a) + ', ' + str(b) + ', ' + str(c)] = func(a, b, c)
            return result
        return wrapper
    return deco


@json_deco('to_json.json')
@csv_reading_deco('random_nums.csv')
def quadratic_equation(a: int, b: int, c: int):
    if a == 0:
        return linear_equation(b, c)
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        x1 = (- b + sqrt(discriminant)) / (2 * a)
        x2 = (- b - sqrt(discriminant)) / (2 * a)
        return round(x1, 2), round(x2, 2)
    elif discriminant == 0:
        x = (- b - sqrt(discriminant)) / (2 * a)
        return round(x, 2)
    return f'No roots'


def generate_random_nums_to_csv(path: str, lines_num: int):
    with open(path, 'w', newline='', encoding='utf-8') as f:
        csv_write = csv.writer(f, dialect='excel-tab', delimiter=' ')
        while lines_num:
            random_nums = [random.randint(-100, 100) for _ in range(3)]
            csv_write.writerow(random_nums)
            lines_num -= 1


def linear_equation(b: int, c: int):
    if b == 0:
        return f'Поскольку а = 0, уравнение линеарное. Уравнение не имеет решений'
    x = -c / b
    return f'Поскольку а = 0, уравнение линеарное. Корень уравнения = {x}'


generate_random_nums_to_csv('random_nums.csv', 100)
quadratic_equation()

