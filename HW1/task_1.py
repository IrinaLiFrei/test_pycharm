# Выведите на консоль таблицу умножения от 2х2 до 9х10 как на школьной тетради

def multiplication_table():
    for i in range(2, 10):
        print()
        for j in range(2, 11):
            print(f"{i} * {j} = {i*j}")
    print()


multiplication_table()

