
def count_characters(string):
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


def main():
    string = input("Enter a string: ")

    char_count = count_characters(string)

    for char, count in char_count.items():
        print(f"{char},{count}")



if __name__ == "__main__":
    main()
