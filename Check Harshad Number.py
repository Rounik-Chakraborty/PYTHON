# Function to check if a number is a Harshad number
def is_harshad_number(number):
    # Calculate the sum of digits
    digit_sum = sum(int(digit) for digit in str(number))
    
    # Check if the number is divisible by the sum of its digits
    return number % digit_sum == 0

# Main code
if __name__ == "__main__":
    # Input from the user
    num = int(input("Enter a number: "))
    
    # Call the function and display the result
    if is_harshad_number(num):
        print(num, "is a Harshad number.")
    else:
        print(num, "is not a Harshad number.")
