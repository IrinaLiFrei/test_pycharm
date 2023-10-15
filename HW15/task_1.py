# 📌Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
# 📌Соберите информацию о содержимом в виде объектов namedtuple.
# 📌Каждый объект хранит:
# ○ имя файла без расширения или название каталога,
# ○ расширение, если это файл,
# ○ флаг каталога,
# ○ название родительского каталога.
# 📌В процессе сбора сохраните данные в текстовый файл используя логирование.

import argparse
import logging
import os


logger = logging.getLogger(__name__)
FORMAT = '{levelname:<10} - {msg}'
logging.basicConfig(filename='task_1.log', encoding='UTF-8', level=logging.INFO, style='{', format=FORMAT)
TYPE = ['file', 'directory']


def walk_directory(path: str = os.getcwd()):
    dir_list = []
    if not os.path.exists(path):
        logger.error(msg=f'Path {path} does not exists')
        logger.warning(msg='Since the path was not found, the path to the current folder was used')
        walk_directory(os.getcwd())
    else:
        for files in os.walk(path):
            for file_ in files[2]:
                parent_dir = files[0].split('\\')[-1]
                file_path = os.path.join(files[0], file_)
                file_size = os.path.getsize(file_path)
                file = {'NAME': file_, 'TYPE': TYPE[0], 'PARENT DIR': parent_dir, 'SIZE': file_size}
                dir_list.append(file)
                logger.info(msg=f'NAME: {file_}, TYPE: {TYPE[0]}, PARENT DIR: {parent_dir}, SIZE: {file_size}')
            for dir_ in files[1]:
                parent_dir = files[0].split('\\')[-1]
                dir_path = os.path.join(files[0], dir_)
                dir_size = get_dir_size(dir_path)
                direc = {'NAME': dir_, 'TYPE': TYPE[1], 'PARENT DIR': parent_dir, 'SIZE': dir_size}
                dir_list.append(direc)
                logger.info(msg=f'NAME: {dir_}, TYPE: {TYPE[1]}, PARENT DIR: {parent_dir}, SIZE: {dir_size}')
        for el in dir_list:
            print(el)
    return dir_list


def get_dir_size(directory):
    dir_size = 0
    for files in os.walk(directory):
        for file in files[2]:
            path = os.path.join(files[0], file)
            dir_size += os.path.getsize(path)
    return dir_size


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='The function returns info about the directory at the entered path',
                                     epilog='Details about the directory are in the log file in the same directory')
    parser.add_argument('path', metavar='path(str)', type=str, nargs=1,
                        help='Enter the path to the desired directory')
    args = parser.parse_args()
    print(walk_directory(*args.path))
