def sum_of_digits(n):
    sum = 0
    while n > 0:
        digit = n % 10
        sum += digit
        n //= 10
    return sum

num = int(input("Enter a number: "))
result = sum_of_digits(num)
print(f"The sum of digits of {num} is {result}")