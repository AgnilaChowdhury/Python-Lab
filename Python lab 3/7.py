import math

def compute_cosine(x, n):
    cosine = 0
    for i in range(n):
        term = ((-1) ** i) * (x ** (2 * i)) / math.factorial(2 * i)
        cosine += term
    return cosine

x = float(input("Enter the value of x (in radians): "))
n = int(input("Enter the number of terms (n): "))

result = compute_cosine(x, n)
print(f"The cosine of {x} using {n} terms is approximately: {result}")
