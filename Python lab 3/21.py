def is_prime(num):

    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


def display_primes(start, end):

    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=' ')

try:
    start = int(input("Enter the start of the interval: "))
    end = int(input("Enter the end of the interval: "))

    if start > end:
        print("The start of the interval must be less than or equal to the end.")
    else:
        print(f"Prime numbers between {start} and {end}:")
        display_primes(start, end)
except ValueError:
    print("Invalid input. Please enter integer values.")
