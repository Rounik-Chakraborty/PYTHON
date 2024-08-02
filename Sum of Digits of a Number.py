# Function to calculate the sum of digits of a number
def sum_of_digits(number):
    # Initialize the sum to 0
    total_sum = 0
    
    # Iterate over each character in the string representation of the number
    for digit in str(number):
        # Convert the character to an integer and add it to the total_sum
        total_sum += int(digit)
    
    return total_sum

# Main code
if __name__ == "__main__":
    # Input from the user
    num = int(input("Enter a number: "))
    
    # Call the function and display the result
    result = sum_of_digits(num)
    print("The sum of digits of", num, "is", result)
