def reverse_list(arr):
    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr

sample_list = [1, 3, 4, 'a', 'b', 'c']
reversed_sample_list = reverse_list(sample_list)
print(reversed_sample_list)
