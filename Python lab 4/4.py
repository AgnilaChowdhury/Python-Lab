
def remove_duplicates_and_sort(words):
    unique_words = set(words)
    sorted_words = sorted(unique_words)
    return sorted_words

def main():
    sequence = input("Enter a sequence of whitespace-separated words: ")
    words = sequence.split()

    sorted_unique_words = remove_duplicates_and_sort(words)

    print(" ".join(sorted_unique_words))


if __name__ == "__main__":
    main()
