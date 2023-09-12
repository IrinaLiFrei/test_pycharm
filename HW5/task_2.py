# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

def split_path(path_str: str):
    slash = len(path_str) - 1 - path_str[::-1].index('\\')
    file_path = path_str[:slash].replace('\\', '/')
    name = path_str[slash + 1:]
    dot = name.index('.')
    file_name = name[:dot]
    file_extension = name[dot + 1:]
    return file_path, file_name, file_extension


path = r'C:\home\user\airin\documents\studies\test.txt'
print(split_path(path))

