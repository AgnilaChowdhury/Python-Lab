def reverse_number(n):
    reversed_n = 0
    while n > 0:
        digit = n % 10
        reversed_n = reversed_n * 10 + digit
        n //= 10
    return reversed_n

n = int(input("Enter a number: "))
result = reverse_number(n)
print("The reverse of", n, "is:", result)