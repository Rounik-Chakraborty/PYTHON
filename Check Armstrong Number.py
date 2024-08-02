# Function to check if the number is an Armstrong number
def is_armstrong(number):
    # Convert the number to a string to easily iterate over digits
    num_str = str(number)
    # Get the number of digits
    num_length = len(num_str)
    # Calculate the sum of digits each raised to the power of the number of digits
    sum_of_digits = sum(int(digit) ** num_length for digit in num_str)
    # Check if the sum is equal to the original number
    return sum_of_digits == number

# Input from the user
number = int(input("Enter a number: "))

# Check if the number is an Armstrong number
if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
