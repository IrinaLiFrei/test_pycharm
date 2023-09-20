import os

from task_1 import generate_files
from task_2 import sort_files
from task_3 import rename_files


if __name__ == '__main__':

    extensions = ['txt', 'pdf', 'json', 'jpg']
    counts = [2, 3, 1, 4]

    generate_files('dir_1', extensions, counts)

    # sort_files('dir_2')

    rename_files('dir_3', 'test', 3, 'jpg', 'txt', [2, 6])


