def sum_of_evens(arr):
    return sum(x for x in arr if x % 2 == 0)

arr = [1, 2, 3, 4, 5, 6]
even_sum = sum_of_evens(arr)
print(even_sum)
