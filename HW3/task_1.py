# 1. Три друга взяли вещи в поход. Сформируйте словарь, где ключ - имя друга, а значение - кортеж вещей.
# Ответьте на вопросы:
# - какие вещи взяли все три друга
# - какие вещи уникальны, есть только у одного друга
# - какие вещи есть у всех друзей, кроме одного, и имя того, у кого данная вещь отсутствует
# Для решения используйте операции со множествами. Код должен расширяться на любое большее количество друзей.
from pprint import pp

friends = {}
items_count = {}
common_items = []
unique_items = []
not_unique_items = []

friends_num = int(input('Введите количество друзей: '))

for i in range(friends_num):
    friend_name = input(f'Введите имя друга {i + 1}: ')
    friend_items = input(f'Введите через запятую вещи, которые взял {friend_name}: ').split(', ')
    friends[friend_name] = tuple(friend_items)

names = set(friends.keys())

for items in friends.values():
    for item in items:
        items_count[item] = items_count.get(item, 0) + 1

for item, count in items_count.items():
    if count == len(friends):
        common_items.append(item)
    elif count == 1:
        unique_items.append(item)
    elif count == len(friends) - 1:
        not_unique_items.append(item)

print(f'Вещи, которые взяли все друзья: {common_items}')
print(f'Уникальные вещи, которые взял только один из друзей: {unique_items}')
print(f'Вещи, которые есть у всех друзей, кроме одного: {not_unique_items}')


