# Напишите функцию, принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хэшируем, используйте его строковое представление.


def get_kwargs_dict(**kwargs):
    kwargs_dict = {}
    for key, value in kwargs.items():
        if is_hashable(value):
            kwargs_dict[value] = key
        else:
            kwargs_dict[str(value)] = key
    return kwargs_dict


def is_hashable(obj):
    try:
        hash(obj)
        return True
    except TypeError:
        return False


dictionary = get_kwargs_dict(int=50, lst=[1, 2, 3, 4, 5], str='string', bool=True)
print(dictionary)
