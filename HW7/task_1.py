# Дорабатываем функции из предыдущих задач.
# Генерируйте файлы в указанную директорию — отдельный параметр функции.
# Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).
# Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

import random
import string
import os


def _create_files(directory: str, extension: str, min_len: int = 6, max_len: int = 15,
                  min_bytes: int = 256, max_bytes: int = 4096, count: int = 42):
    for i in range(count):
        name_len = random.randint(min_len, max_len)
        filename = ''.join(random.choices(string.ascii_letters, k=name_len)).lower()
        cnt = 1
        while os.path.exists(os.path.join(directory, filename + extension)):
            filename += '_' + f'{cnt}'
            cnt += 1
        filename += f'.{extension}'

        num_bytes = random.randint(min_bytes, max_bytes)
        data = random.randbytes(num_bytes)

        with open(os.path.join(directory, filename), 'wb') as f:
            f.write(data)


def generate_files(dir_: str, extensions: list, counts: list):
    if not os.path.exists(dir_):
        os.makedirs(dir_)
    for extension, count in zip(extensions, counts):
        _create_files(dir_, extension, count=count)
