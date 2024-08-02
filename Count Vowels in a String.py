def count_vowels(input_string):
    # Define a set of vowels
    vowels = "aeiouAEIOU"
    
    # Initialize a counter for vowels
    count = 0
    
    # Loop through each character in the input string
    for char in input_string:
        # Check if the character is a vowel
        if char in vowels:
            count += 1
    
    return count

# Input string from the user
input_string = input("Enter a string: ")

# Call the function and print the result
print(f"The number of vowels in the string is: {count_vowels(input_string)}")
