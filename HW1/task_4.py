# 4. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.
# Для генерации случайного числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000

num = randint(LOWER_LIMIT, UPPER_LIMIT)

attempts = 10

print("Угадайте число от 0 до 1000. У вас есть 10 попыток.")

while attempts > 0:
    your_num = int(input("Введите число: "))

    if your_num < num:
        print("Загаданное число больше")
    elif your_num > num:
        print("Загаданное число меньше")
    else:
        print("Вы угадали загаданное число!")
        break

    attempts -= 1

else:
    print("У вас закончились попытки. Было загадано число: ", num)
