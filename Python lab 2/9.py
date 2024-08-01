def decimal_to_binary(n):
    if n == 0:
        return '0'
    result = ''
    while n > 0:
        result = str(n % 2) + result
        n = n // 2
    return result

decimal_num = int(input("Enter a decimal number: "))
binary_num = decimal_to_binary(decimal_num)
print(f"The binary representation of {decimal_num} is {binary_num}")