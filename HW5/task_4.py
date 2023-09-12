# Создайте функцию генератор чисел Фибоначчи (см. Википедию).
# Функция ничего не принимает, бесконечно генерирует каждое последующее число, использовать yield

def fibonacci():
    a = 0
    b = 1
    yield b
    while True:
        yield a + b
        a, b = b, a + b


generator = fibonacci()

for num in generator:
    print(num)


