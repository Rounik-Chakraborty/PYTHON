# Function to calculate the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

# Take the number as input from the user
number = int(input("Enter a non-negative integer: "))

# Ensure the number is non-negative
if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    # Calculate the factorial
    fact = factorial(number)
    
    # Print the result
    print(f"The factorial of {number} is: {fact}")
