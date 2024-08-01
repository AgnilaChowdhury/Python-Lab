def alternating_series(n):
    if n <= 0:
        return "n must be a positive integer."

    total = 0
    for i in range(1, n + 1):
        term = 1 / i
        if i % 2 == 0:
            total -= term
        else:
            total += term
    return total

n = int(input("Enter a positive integer: "))
result = alternating_series(n)
print(f"The sum of the series up to {n} terms is: {result}")
