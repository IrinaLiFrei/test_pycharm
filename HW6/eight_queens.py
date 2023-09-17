# Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей
# в задаче выше. Проверяйте различный случайные варианты и выведите 4 успешных расстановки.

import random


def horizontal_check(matrix):
    for i in range(len(matrix)):
        sum_horizontal = 0
        for j in range(len(matrix)):
            sum_horizontal += matrix[i][j]
        if sum_horizontal > 1:
            return False
    return True


def vertical_check(matrix):
    for j in range(len(matrix)):
        sum_vertical = 0
        for i in range(len(matrix)):
            sum_vertical += matrix[i][j]
            if sum_vertical > 1:
                return False
    return True


def diagonal_check(matrix):
    sum_main_diagonal = 0
    sum_side_diagonal = 0

    for i in range(len(matrix)):
        sum_main_diagonal += matrix[i][i]
        sum_side_diagonal += matrix[i][len(matrix) - 1 - i]
        if sum_main_diagonal > 1 or sum_side_diagonal > 1:
            return False

    for k in range(1, len(matrix)):
        sum_upper_diagonal = 0
        sum_lower_diagonal = 0

        for i in range(len(matrix) - k):
            j = i + k
            sum_upper_diagonal += matrix[i][j]
            sum_lower_diagonal += matrix[j][i]
            if sum_upper_diagonal > 1 or sum_lower_diagonal > 1:
                return False
    return True


def arrange_board(a, a1, b, b1, c, c1, d, d1, e, e1, f, f1, g, g1, h, h1):
    chess_board = [[0 for j in range(8)] for i in range(8)]
    chess_board[a-1][a1-1] = 1
    chess_board[b-1][b1-1] = 1
    chess_board[c-1][c1-1] = 1
    chess_board[d-1][d1-1] = 1
    chess_board[e-1][e1-1] = 1
    chess_board[f-1][f1-1] = 1
    chess_board[g-1][g1-1] = 1
    chess_board[h-1][h1-1] = 1
    # print(chess_board)
    _print_board(chess_board)
    return check_board(chess_board)


def check_board(matrix):
    if horizontal_check(matrix) and vertical_check(matrix) and diagonal_check(matrix):
        return True
    return False


def _print_board(matrix):
    for row in matrix:
        print('  '.join(map(str, row)))


def generate_board():
    chess_board = [[0 for j in range(8)] for i in range(8)]
    n = 4
    while n > 0:
        for i in range(8):
            j = random.randint(0, 7)
            chess_board[i][j] = 1
        if check_board(chess_board):
            _print_board(chess_board)
            n -= 1


if __name__ == '__main__':
    print(arrange_board(2, 5, 6, 1, 7, 3, 6, 3, 5, 1, 2, 4, 1, 1, 8, 3))
    bad_position = [[1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0]]
    print(f'{horizontal_check(bad_position)=}')
    print(f'{vertical_check(bad_position)=}')
    print(f'{diagonal_check(bad_position)=}')
    print(arrange_board(1, 4, 2, 7, 3, 3, 4, 8, 5, 2, 6, 5, 7, 1, 8, 6))
    good_position = [[0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0]]
    print(f'{horizontal_check(good_position)=}')
    print(f'{vertical_check(good_position)=}')
    print(f'{diagonal_check(good_position)=}')
    print()
    print('4 random good positions: ')
    generate_board()

