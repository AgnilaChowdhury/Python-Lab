def print_multiples_of_ten(start, end):
    if end <= 9:
        print(f"There are no multiples of 10 between {start} and {end}")
    else:
        print(f"Multiples of 10 between {start} and {end} are:")
        for i in range(start, end + 1):
            if i % 10 == 0:
                print(i)

start = int(input("Enter the start of the interval: "))
end = int(input("Enter the end of the interval: "))

print_multiples_of_ten(start, end)