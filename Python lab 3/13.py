def count_digits(n):
    return len(str(abs(n)))

number = int(input("Enter an integer: "))
digit_count = count_digits(number)
print(f"The number of digits in {number} is: {digit_count}")
