# Допишите в вашу задачу Archive обработку исключений.
# Добавьте исключение в ваш код InvalidTextError, которые будет вызываться, когда текст не является строкой или
# является пустой строкой.
# И InvalidNumberError, которое будет вызываться, если число не является положительным целым числом
# или числом с плавающей запятой.

from typing import Union
class Archive:

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.archive_text = []
            cls._instance.archive_number = []
        else:
            cls._instance.archive_text.append(cls._instance.text)
            cls._instance.archive_number.append(cls._instance.number)
        return cls._instance

    def __init__(self, text: str, number: Union[int, float]):
        if not isinstance(text, str) or text == '':
            raise InvalidTextError(text)
        self.text = text
        if (not isinstance(number, int) and not isinstance(number, float)) or number <= 0:
            raise InvalidNumberError(number)
        self.number = number

    def __str__(self):
        return f'Text is {self.text} and number is {self.number}. Also {self.archive_text} and {self.archive_number}'

    def __repr__(self):
        return f'Archive("{self.text}", {self.number})'




class OwnBaseError(Exception):
    def __init__(self, message: str):
        self.message = message

    def __str__(self):
        return self.message


class InvalidTextError(OwnBaseError):
    def __init__(self, name: str):
        super(InvalidTextError, self).__init__(f'Invalid text: {name}. Text should be a non-empty string.')


class InvalidNumberError(OwnBaseError):
    def __init__(self, value: int):
        super(InvalidNumberError, self).__init__(f'Invalid number: {value}. Number should be a positive integer or float.')



archive_instance = Archive("Sample text", 42.5)
print(archive_instance)
# invalid_archive_instance = Archive("", 5)
# print(invalid_archive_instance)
# invalid_archive_instance = Archive("Sample text", -5)
# print(invalid_archive_instance)
