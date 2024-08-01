def print_series(n):
    term = 1
    for i in range(1, n + 1):
        print(f"Term {i}: {term}")
        term *= i

n = int(input("Enter the number of terms: "))
print("Series:")
print_series(n)