# Function to reverse the string
def reverse_string(string):
    return string[::-1]

# Function to check whether the string is a palindrome
def is_palindrome(string):
    reversed_string = reverse_string(string)
    return string == reversed_string

# Function to check whether the string ends with a specific substring
def ends_with_substring(string, substring):
    return string.endswith(substring)

# Function to capitalize the first letter of each word in the string
def capitalize_words(string):
    return string.title()

# Function to check if two strings are anagrams
def is_anagram(string1, string2):
    return sorted(string1) == sorted(string2)

# Function to remove vowels from a string
def remove_vowels(string):
    vowels = "aeiouAEIOU"
    return ''.join([char for char in string if char not in vowels])

# Function to find the length of the longest word in a sentence
def length_of_longest_word(sentence):
    words = sentence.split()
    return max(len(word) for word in words)

# Main function
def main():
    # Accept input from the user
    string = input("Enter a string: ")

    # Reverse the string
    reversed_str = reverse_string(string)
    print(f"Reversed String: {reversed_str}")

    # Check if the string is a palindrome
    if is_palindrome(string):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")

    # Check if the string ends with a specific substring
    substring = input("Enter a substring to check if the string ends with it: ")
    if ends_with_substring(string, substring):
        print(f"The string ends with '{substring}'.")
    else:
        print(f"The string does not end with '{substring}'.")

    # Capitalize the first letter of each word
    capitalized_str = capitalize_words(string)
    print(f"Capitalized String: {capitalized_str}")

    # Check if two strings are anagrams
    string2 = input("Enter another string to check if it's an anagram: ")
    if is_anagram(string, string2):
        print(f"The strings '{string}' and '{string2}' are anagrams.")
    else:
        print(f"The strings '{string}' and '{string2}' are not anagrams.")

    # Remove vowels from the string
    no_vowels_str = remove_vowels(string)
    print(f"String without vowels: {no_vowels_str}")

    # Find the length of the longest word in a sentence
    longest_word_length = length_of_longest_word(string)
    print(f"Length of the longest word: {longest_word_length}")

# Execute the main function
if __name__ == "__main__":
    main()
