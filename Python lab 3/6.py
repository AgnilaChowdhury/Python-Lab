import math

def compute_sine(x, n):
    sine = 0
    for i in range(n):
        term = ((-1) ** i) * (x ** (2 * i + 1)) / math.factorial(2 * i + 1)
        sine += term
    return sine

x = float(input("Enter the value of x (in radians): "))
n = int(input("Enter the number of terms (n): "))

result = compute_sine(x, n)
print(f"The sine of {x} using {n} terms is approximately: {result}")
