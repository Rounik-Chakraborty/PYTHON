# Function to check if a number is an automorphic number
def is_automorphic(number):
    # Calculate the square of the number
    square = number * number
    
    # Convert both number and square to strings to compare digits
    number_str = str(number)
    square_str = str(square)
    
    # Check if the square ends with the number
    return square_str.endswith(number_str)

# Take the number as input from the user
number = int(input("Enter a number: "))

# Check if the number is automorphic
if is_automorphic(number):
    print(f"{number} is an automorphic number.")
else:
    print(f"{number} is not an automorphic number.")
