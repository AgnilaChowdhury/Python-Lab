def print_table():
    num_rows = 5

    print("1 1 1 1 1")

    for i in range(2, num_rows + 1):
        col1 = i
        col2 = 1
        col3 = i
        col4 = i ** 2
        col5 = i ** 3
        print(f"{col1} {col2} {col3} {col4} {col5}")

print_table()
