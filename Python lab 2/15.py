def calculate_power(base, exponent):
    result = 1
    for _ in range(abs(exponent)):
        result *= base
    if exponent < 0:
        return 1 / result
    else:
        return result

base = float(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))

print(f"The power of {base} to {exponent} is: {calculate_power(base, exponent)}")