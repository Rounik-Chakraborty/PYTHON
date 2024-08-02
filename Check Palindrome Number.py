# Function to check if a number is a palindrome
def is_palindrome(number):
    # Convert the number to a string
    num_str = str(number)
    # Check if the string is equal to its reverse
    return num_str == num_str[::-1]

# Main code
if __name__ == "__main__":
    # Input from the user
    num = int(input("Enter a number: "))
    
    # Call the function and display the result
    if is_palindrome(num):
        print(num, "is a palindrome.")
    else:
        print(num, "is not a palindrome.")
