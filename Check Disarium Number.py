# Function to check if a number is a Disarium number
def is_disarium_number(number):
    # Convert the number to a string to process each digit
    num_str = str(number)
    total_sum = 0
    
    # Iterate over each digit and its position (1-based index)
    for index, digit in enumerate(num_str):
        # Convert the digit to an integer and raise it to the power of its position
        total_sum += int(digit) ** (index + 1)
    
    # Check if the sum is equal to the original number
    return total_sum == number

# Main code
if __name__ == "__main__":
    # Input from the user
    num = int(input("Enter a number: "))
    
    # Call the function and display the result
    if is_disarium_number(num):
        print(num, "is a Disarium number.")
    else:
        print(num, "is not a Disarium number.")
