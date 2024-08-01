def check_number(n):
    return n % 7 == 0 and n % 5 != 0

def find_numbers():

    result = []
    for num in range(1000, 2001):
        if check_number(num):
            result.append(num)
    return result

numbers = find_numbers()
print(numbers)
