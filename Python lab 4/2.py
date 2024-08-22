def sort_words(sequence):
    words = sequence.split(",")
    words.sort()
    return ",".join(words)

def main():
    sequence = input("Enter a comma-separated sequence of words: ")
    sorted_sequence = sort_words(sequence)
    print(f"The sorted sequence is: {sorted_sequence}")

if __name__ == "__main__":
    main()
