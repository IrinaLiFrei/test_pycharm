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
import stat
from collections import namedtuple

logger = logging.getLogger(__name__)
FORMAT = '{levelname:<10} - {msg}'
logging.basicConfig(filename='task_1_version_2.log', encoding='UTF-8', level=logging.INFO, style='{', format=FORMAT)


def walk_directory(path: str):
    if not os.path.exists(path):
        logger.error(msg=f'Path {path} does not exists')
        logger.warning(msg='Since the path was not found, the path to the current folder was used')
        walk_directory(os.getcwd())
    else:
        for files in os.walk(path):
            for file_ in files[2]:
                parent_dir = files[0].split('\\')[-1]
                file_name = file_.split('.')[0]
                extension = file_.split('.')[1]
                FileInfo = namedtuple('FileInfo', ['file_name', 'extension', 'parent_dir'])
                file_info = FileInfo(file_name, extension, parent_dir)
                logger.info(msg=f'FILE NAME: {file_info.file_name}, EXTENSION: {file_info.extension}, PARENT DIR: {file_info.parent_dir}')
            for dir_ in files[1]:
                parent_dir = files[0].split('\\')[-1]
                dir_path = os.path.join(files[0], dir_)
                flag_ = get_flag(dir_path)
                DirInfo = namedtuple('DirInfo', ['dir_name', 'flag', 'parent_dir'])
                dir_info = DirInfo(dir_, flag_, parent_dir)
                logger.info(msg=f'DIRECTORY NAME: {dir_info.dir_name}, FLAG: {dir_info.flag}, PARENT DIR: {dir_info.parent_dir}')


def get_flag(directory):
    flag_list = []
    if os.stat(directory).st_mode & stat.S_IRUSR:
        flag_list.append('r')
    else:
        flag_list.append('-')
    if os.stat(directory).st_mode & stat.S_IWUSR:
        flag_list.append('w')
    else:
        flag_list.append('-')
    if os.stat(directory).st_mode & stat.S_IXUSR:
        flag_list.append('x')
    else:
        flag_list.append('-')
    return flag_list


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='The function returns info about the directory at the entered path',
                                     epilog='Details about the directory are in the log file in the same directory')
    parser.add_argument('path', metavar='path(str)', type=str, nargs=1,
                        help='Enter the path to the desired directory')
    args = parser.parse_args()
    print(walk_directory(*args.path))
