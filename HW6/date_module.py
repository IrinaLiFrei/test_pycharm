# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты: год может быть в диапазоне [1, 9999]. Весь период (1 января 1 года - 31 декабря 9999 года)
# действует Григорианский календарь. Проверку года на високосность вынести в отдельную защищённую функцию.
#
# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

import sys


def _is_leap(year: int):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    return False


def check_date(date_input: str) -> bool:
    day, month, year = map(int, date_input.split('.'))
    days = {1: 31, 2: 29 if _is_leap(year) else 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31,
            8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if day < 1 or day > days[month]:
        return False
    if month < 1 or month > 12:
        return False
    if year < 1 or year > 9999:
        return False
    return True


if __name__ == '__main__':
    # print(check_date('29.02.2024'))
    check_input = sys.argv[1:]
    date_to_check = check_input[0]
    if check_date(date_to_check):
        print('True')
    else:
        print('False')

