
def filter_digit_words(words):
    digit_words = [word for word in words if word.isdigit()]
    return digit_words

def main():
    sentence = input("Enter a sequence of words separated by whitespace: ")
    words = sentence.split()
    digit_words = filter_digit_words(words)
    print(digit_words)


if __name__ == "__main__":
    main()
