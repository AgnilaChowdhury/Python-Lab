
def count_letters_and_digits(sentence):
    letters = 0
    digits = 0

    for char in sentence:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1

    return letters, digits


def main():
    sentence = input("Enter a sentence: ")

    letters, digits = count_letters_and_digits(sentence)

    print(f"LETTERS {letters}")
    print(f"DIGITS {digits}")


if __name__ == "__main__":
    main()
