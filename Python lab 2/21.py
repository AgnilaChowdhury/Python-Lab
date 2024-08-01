def sum_of_natural_numbers(n):
    return sum(range(1, n+1))

n = int(input("Enter a range: "))
print("The sum of natural numbers up to", n, "is:", sum_of_natural_numbers(n))