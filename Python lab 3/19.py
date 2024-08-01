def is_multiple(m, n):
    if n == 0:
        return False
    return m % n == 0

try:
    m = int(input("Enter the value of m: "))
    n = int(input("Enter the value of n: "))

    if is_multiple(m, n):
        print(f"{m} is a multiple of {n}.")
    else:
        print(f"{m} is not a multiple of {n}.")
except ValueError:
    print("Invalid input. Please enter integer values.")
