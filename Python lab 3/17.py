def find_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)

    if n % 2 == 1:
        return sorted_numbers[n // 2]
    else:
        mid1 = sorted_numbers[n // 2 - 1]
        mid2 = sorted_numbers[n // 2]
        return (mid1 + mid2) / 2

numbers = list(map(float, input("Enter a set of numbers separated by spaces: ").split()))
median = find_median(numbers)
print(f"The median is: {median}")
