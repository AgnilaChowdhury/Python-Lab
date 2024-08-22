import numpy as np

def sum_of_diagonals(matrix):
    return np.trace(matrix)

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
diagonal_sum = sum_of_diagonals(matrix)
print(diagonal_sum)
