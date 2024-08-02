# Program to find the factorial of a number

# Function to calculate factorial
def factorial(n):
    if n < 0:
        return "Factorial does not exist for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact

# Input from user
num = int(input("Enter a number: "))

# Calculate and display the factorial
result = factorial(num)
print(f"The factorial of {num} is {result}")
