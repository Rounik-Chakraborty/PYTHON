# Function to reverse a number
def reverse_number(number):
    # Convert the number to a string and remove the negative sign if present
    num_str = str(number).lstrip('-')
    # Reverse the string and convert it back to an integer
    reversed_num = int(num_str[::-1])
    
    # If the original number was negative, return the negative of the reversed number
    if number < 0:
        reversed_num = -reversed_num
    
    return reversed_num

# Main code
if __name__ == "__main__":
    # Input from the user
    num = int(input("Enter a number: "))
    
    # Call the function and display the result
    result = reverse_number(num)
    print("The reversed number is", result)
