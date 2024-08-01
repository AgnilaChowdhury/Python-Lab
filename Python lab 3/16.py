def binary_to_decimal(binary_str):

    return int(binary_str, 2)

def decimal_to_binary(decimal_num):

    return bin(decimal_num)[2:]

binary_str = input("Enter a binary number: ")
try:
    decimal_result = binary_to_decimal(binary_str)
    print(f"The decimal representation of binary {binary_str} is: {decimal_result}")
except ValueError:
    print("Invalid binary number.")

decimal_num = int(input("Enter a decimal number: "))
binary_result = decimal_to_binary(decimal_num)
print(f"The binary representation of decimal {decimal_num} is: {binary_result}")
