# Напишите функцию группового переименования файлов. Она должна:
# - принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# - принимать параметр количество цифр в порядковом номере.
# - принимать параметр расширение исходного файла. Переименование должно работать
# только для этих файлов внутри каталога.
# - принимать параметр расширение конечного файла.
# - принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6]
#  берутся буквы с 3 по 6 из исходного имени файла.
#  К ним прибавляется желаемое конечное имя, если оно передано.
#  Далее счётчик файлов и расширение.

import os


def rename_files(directory: str, name: str, digits_count: int, extension_src: str, extension_dst, section=None):
    path_ = os.path.join(os.getcwd(), directory)
    ext_list = []
    count = 1
    dir_list = os.listdir(path_)

    if section is None:
        section = [3, 6]

    for el in dir_list:
        extension = os.path.splitext(el)[1]
        if extension == '.' + extension_src:
            ext_list.append(el)

    for item in ext_list:
        nulls = str(count).rjust(digits_count, '0')
        new_name = f'{item[section[0] - 1:section[1]]}' + '_' + f'{name}' + f'{nulls}' + '.' + f'{extension_dst}'
        os.rename(os.path.join(path_, item), os.path.join(path_, new_name))
        count += 1

