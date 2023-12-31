# 4. Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

MAX_WEIGHT = 12
items_dict = {
            'палатка': 5,
            'посуда': 3,
            'бутылка с водой': 3,
            'одежда': 3,
            'аптечка': 1,
            'еда': 4
            }

items_set = {}
set_weight = 0

for key, value in items_dict.items():
    if (set_weight + value) <= MAX_WEIGHT:
        items_set.setdefault(key, value)
        set_weight += value

print(items_set)
