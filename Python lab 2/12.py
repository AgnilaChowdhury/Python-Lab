def print_multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

num = int(input("Enter a number: "))
print(f"Multiplication table of {num}:")
print_multiplication_table(num)