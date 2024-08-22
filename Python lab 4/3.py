# Function to capitalize each line in the sequence
def capitalize_lines(lines):
    capitalized_lines = [line.upper() for line in lines]  # Convert each line to uppercase
    return capitalized_lines


# Main function
def main():
    print("Enter the lines (type 'END' to finish):")
    lines = []

    while True:
        line = input()  # Take input line by line
        if line == "END":  # Condition to stop taking input
            break
        lines.append(line)

    capitalized_lines = capitalize_lines(lines)  # Capitalize the lines

    print("\nCapitalized lines:")
    for line in capitalized_lines:
        print(line)  # Print each capitalized line


# Execute the main function
if __name__ == "__main__":
    main()
