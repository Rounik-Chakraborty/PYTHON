# Function to find the ASCII value of a character
def get_ascii_value(character):
    return ord(character)

# Take a character as input from the user
char = input("Enter a character: ")

# Ensure the input is a single character
if len(char) != 1:
    print("Please enter a single character.")
else:
    # Get the ASCII value
    ascii_value = get_ascii_value(char)
    
    # Print the result
    print(f"The ASCII value of '{char}' is {ascii_value}")
