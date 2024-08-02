def is_neon_number(number):
    # Calculate the square of the number
    square = number * number
    
    # Calculate the sum of the digits of the square
    sum_of_digits = sum(int(digit) for digit in str(square))
    
    # Check if the sum of the digits is equal to the number
    if sum_of_digits == number:
        return True
    else:
        return False

# Input from user
number = int(input("Enter a number: "))

# Check if the number is a neon number
if is_neon_number(number):
    print(f"{number} is a neon number.")
else:
    print(f"{number} is not a neon number.")
