# Создать функцию-генератор. Функция генерирует N простых чисел, начиная с числа 2.
# Для проверки числа на простоту использовать правило: число является простым, если делится
# только на единицу и на себя. В функции использовать yield

def generate_prime_nums(num: int):
    count = 0
    number = 2
    while count < num:
        is_prime = True
        for i in range(2, number//2 + 1):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            count += 1
            yield number
        number += 1


print(*(generate_prime_nums(10)))



