# Реализуйте класс Matrix, представляющий матрицу и поддерживающий следующие операции:
#
# Инициализация матрицы. Конструктор класса должен принимать количество строк rows и
# количество столбцов cols и создавать матрицу с нулевыми значениями.
#
# Операция сложения матриц. Реализуйте метод __add__, который позволяет складывать две
# матрицы одинаковых размеров.
#
# Операция умножения матриц. Реализуйте метод __mul__, который позволяет умножать две
# матрицы с согласованными размерами (количество столбцов первой матрицы должно быть
# равно количеству строк второй матрицы).
#
# Сравнение матриц на равенство. Реализуйте метод __eq__, который позволяет сравнивать две
# матрицы на равенство.
#
# Представление матрицы в виде строки. Реализуйте метод __str__, который возвращает
# строковое представление матрицы, где элементы строки разделены пробелами, а строки сами
# разделены символами новой строки.
#
# Представление матрицы в виде строки для создания нового объекта. Реализуйте метод __repr__,
# который возвращает строку, которую можно использовать для создания нового объекта класса Matrix.




class Matrix:

    """
    Класс, представляющий матрицу.

    Атрибуты:
    - rows (int): количество строк в матрице
    - cols (int): количество столбцов в матрице
    - data (list): двумерный список, содержащий элементы матрицы

    Методы:
    - __str__(): возвращает строковое представление матрицы
    - __repr__(): возвращает строковое представление матрицы, которое может быть использовано для создания нового объекта
    - __eq__(other): определяет операцию "равно" для двух матриц
    - __add__(other): определяет операцию сложения двух матриц
    - __mul__(other): определяет операцию умножения двух матриц
    """

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0] * cols for _ in range(rows)]

    def __str__(self):
        return '\n'.join([' '.join([str(self.data[i][j]) for j in range(self.cols)]) for i in range(self.rows)])

    def __repr__(self):
        return f"Matrix({self.rows}, {self.cols})"

    def __eq__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            return False
        for i in range(self.rows):
            for j in range(self.cols):
                if self.data[i][j] != other.data[i][j]:
                    return False
        return True

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Матрицы должны иметь одинаковые размеры")
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] + other.data[i][j]
        return result

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Количество столбцов первой матрицы должно быть равно количеству строк второй матрицы")
        result = Matrix(self.rows, other.cols)
        for i in range(result.rows):
            for j in range(result.cols):
                for k in range(self.cols):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]
        return result


m1 = Matrix(2, 3)
m1.data = [[1, 2, 3], [4, 5, 6]]

m2 = Matrix(2, 3)
m2.data = [[7, 8, 9], [10, 11, 12]]

m3 = Matrix(3, 2)
m3.data = [[1, 2], [3, 4], [5, 6]]

print(m1+m2)  # [[8, 10, 12], [14, 16, 18]]
print(m1 * m3)  # [[22, 28], [49, 64]]
print(m1 == m2)   # False
print(m1 == m1)   # True
print(str(m1))
