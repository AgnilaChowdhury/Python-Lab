def print_pattern(N):
    for i in range(1, N + 1):
        print(' ' * (N - i) + '/' + ' ' * (2 * i - 2) + '\\')

    for i in range(1, N + 1):
        print(' ' * (N - i) + '/' + '_' * (2 * i - 2) + '\\')

N = int(input("Enter the number of lines (N): "))
print_pattern(N)
