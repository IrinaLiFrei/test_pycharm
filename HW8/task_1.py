# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle.
# Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория.
# Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных
# файлов и директорий.

import os
import json
import csv
import pickle

CATEGORY = ['file', 'directory']


def walk_directory(path: str = os.getcwd()):
    dir_list = []
    for files in os.walk(path):
        for file in files[2]:
            parent_dir = files[0].split('\\')[-1]
            file_path = os.path.join(files[0], file)
            file_size = os.path.getsize(file_path)
            file = {'NAME': file, 'CATEGORY': CATEGORY[0], 'PARENT DIR': parent_dir, 'SIZE': file_size}
            dir_list.append(file)
        for dir_ in files[1]:
            parent_dir = files[0].split('\\')[-1]
            dir_path = os.path.join(files[0], dir_)
            dir_size = get_dir_size(dir_path)
            dir_ = {'NAME': dir_, 'CATEGORY': CATEGORY[1], 'PARENT DIR': parent_dir, 'SIZE': dir_size}
            dir_list.append(dir_)

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


def save_to_json(path, data):
    with open(path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)


def save_to_csv(path, data):
    csv_headers = list(data[0].keys())
    with open(path, 'w', encoding='utf-8') as cvs_file:
        csv_writer = csv.DictWriter(cvs_file, fieldnames=csv_headers, delimiter=' ', quotechar='|', quoting=csv.QUOTE_NONNUMERIC)
        csv_writer.writeheader()
        csv_writer.writerows(data)


def save_to_pickle(path, data):
    with open(path, 'wb') as pickle_file:
        pickle.dump(data, pickle_file)


data = walk_directory('C:\\Users\\airin\\PycharmProjects\\pythonProject\\HW8')
save_to_json('to_json.json', data)
save_to_csv('to_csv.csv', data)
save_to_pickle('to_pickle.pickle', data)

