def reverse_array(arr):
    n = len(arr)
    for i in range(n // 2):
        arr[i], arr[n - 1 - i] = arr[n - 1 - i], arr[i]

arr = [1, 2, 3, 4, 5]
reverse_array(arr)
print(arr)
