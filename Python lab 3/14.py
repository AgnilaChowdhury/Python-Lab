import math

def calculate_exponential(x):
    return math.exp(x)

x = float(input("Enter the exponent value: "))
result = calculate_exponential(x)
print(f"e^{x} is approximately: {result}")
