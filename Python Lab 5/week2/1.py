def sum_and_average(arr):
    total = sum(arr)
    average = total / len(arr)
    return total, average

arr = [1, 2, 3, 4, 5]
total, average = sum_and_average(arr)
print(f"Sum: {total}, Average: {average}")
