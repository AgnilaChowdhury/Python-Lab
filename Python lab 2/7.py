def reverse(s):
    reversed_s = ""
    for char in s:
        reversed_s = char + reversed_s
    return reversed_s

str = input("Enter the String: ")
print(reverse(str))