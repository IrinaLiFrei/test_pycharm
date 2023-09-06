# 2. Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

import random

new_list = set()
original_list = [random.randint(0, 10) for _ in range(10)]
print(original_list)

for i in original_list:
    if (count := original_list.count(i)) >= 2:
        new_list.add(i)
print(new_list)
