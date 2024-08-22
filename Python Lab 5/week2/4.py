import numpy as np

def sum_of_2d_arrays(arr1, arr2):
    return np.add(arr1, arr2)

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
result = sum_of_2d_arrays(arr1, arr2)
print(result)
