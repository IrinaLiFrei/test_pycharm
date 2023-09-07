# Напишите функцию для транспонирования матрицы

def transpose_matrix(matrix):

    rows = len(matrix)
    columns = len(matrix[0])
    transposed_matrix = [[0 for _ in range(columns)] for _ in range(rows)]
  
    for i in range(rows):
        for j in range(columns):
            transposed_matrix[j][i] = matrix[i][j]

    return transposed_matrix


original_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(original_matrix)
transposed = transpose_matrix(original_matrix)
print(transposed)
