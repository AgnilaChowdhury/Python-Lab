import math

def is_krishnamurthy(n):
    sum = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        sum += math.factorial(digit)
        temp //= 10
    return sum == n

num = int(input("Enter a number: "))
if is_krishnamurthy(num):
    print(f"{num} is a Krishnamurthy number.")
else:
    print(f"{num} is not a Krishnamurthy number.")