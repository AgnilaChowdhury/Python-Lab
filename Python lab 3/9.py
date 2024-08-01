def print_8_segment_display(number):
    segments = {
        '0': [' _ ', '| |', '|_|'],
        '1': ['   ', '  |', '  |'],
        '2': [' _ ', ' _|', '|_ '],
        '3': [' _ ', ' _|', ' _|'],
        '4': ['   ', '|_|', '  |'],
        '5': [' _ ', '|_ ', ' _|'],
        '6': [' _ ', '|_ ', '|_|'],
        '7': [' _ ', '  |', '  |'],
        '8': [' _ ', '|_|', '|_|'],
        '9': [' _ ', '|_|', ' _|']
    }

    number_str = str(number)

    for row in range(3):
        line = ""
        for digit in number_str:
            line += segments[digit][row] + " "
        print(line)


number = input("Enter a number: ")
print_8_segment_display(number)
