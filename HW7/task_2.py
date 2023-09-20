# Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# Каждая группа включает файлы с несколькими расширениями.
# В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

import os
import shutil


def sort_files(directory: str):
    dirs = ['Texts', 'Videos', 'Images']
    for dir_ in dirs:
        if not os.path.exists(dir_):
            os.mkdir(dir_)

    path_ = os.path.join(os.getcwd(), directory)

    path_to_text = os.path.join(path_, 'Texts')
    path_to_video = os.path.join(path_, 'Videos')
    path_to_image = os.path.join(path_, 'Images')

    dir_list = os.listdir(path_)

    for el in dir_list:
        extension = os.path.splitext(el)[1]
        if extension in ['.txt', '.doc']:
            shutil.move(os.path.join(path_, el), path_to_text)
        elif extension in ['.avi', '.mov']:
            shutil.move(os.path.join(path_, el), path_to_video)
        elif extension in ['.jpg', '.jpeg']:
            shutil.move(os.path.join(path_, el), path_to_image)




