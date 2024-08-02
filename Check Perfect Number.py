# Function to check if a number is a perfect number
def is_perfect_number(number):
    if number < 1:
        return False
    
    # Calculate the sum of proper divisors
    sum_of_divisors = sum(i for i in range(1, number) if number % i == 0)
    
    # Check if the sum of divisors is equal to the number
    return sum_of_divisors == number

# Take the number as input from the user
number = int(input("Enter a number: "))

# Check if the number is a perfect number
if is_perfect_number(number):
    print(f"{number} is a perfect number.")
else:
    print(f"{number} is not a perfect number.")
