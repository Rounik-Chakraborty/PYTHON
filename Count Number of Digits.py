# Function to count the number of digits in a number
def count_digits(number):
    # Convert the number to a string and remove the negative sign if present
    num_str = str(number).lstrip('-')
    # Return the length of the string
    return len(num_str)

# Main code
if __name__ == "__main__":
    # Input from the user
    num = int(input("Enter a number: "))
    
    # Call the function and display the result
    result = count_digits(num)
    print("The number of digits in", num, "is", result)
