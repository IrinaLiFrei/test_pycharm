import random


class MyMatrix:
    my_matrix = []

    def __init__(self, columns: int, rows: int):
        self.columns = columns
        self.rows = rows
        if not self._check_matrix():
            raise ValueError('Such matrix can not exist')
        self.create_matrix()

    def _check_matrix(self):
        return self.columns > 0 and self.rows > 0

    def create_matrix(self):
        for row in range(self.rows):
            temp = []
            for column in range(self.columns):
                temp.append(random.randint(1, 100))
            self.my_matrix.append(temp)

    def print_matrix(self):
        for row in range(self.rows):
            for column in range(self.columns):
                print(self.my_matrix[row][column], end='\t')
            print()


matr = MyMatrix(3, 6)
matr.create_matrix()
matr.print_matrix()
