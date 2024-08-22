
def count_word_occurrences(sentence):
    words = sentence.split()
    word_count = {}
    for word in words:
        word = word.strip('.').lower()
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count


def find_substring(sentence, substring):
    if substring in sentence:
        return f"The substring '{substring}' is found in the sentence."
    else:
        return f"The substring '{substring}' is not found in the sentence."



def main():
    sentence = input("Enter a string: ")


    length_of_string = len(sentence)
    print(f"The length of the string is: {length_of_string}")

    substring_result = find_substring(sentence, "country")
    print(substring_result)

    word_count = count_word_occurrences(sentence)
    print("Occurrences of each word in the sentence:")
    for word, count in word_count.items():
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()
