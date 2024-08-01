def is_buzz_number(n):
    if n % 10 == 7 or n % 7 == 0:
        return True
    else:
        return False

num = int(input("Enter a number: "))

if is_buzz_number(num):
    print(f"{num} is a Buzz number.")
else:
    print(f"{num} is not a Buzz number.")