# Function to calculate power of a number
def calculate_power(base, exponent):
    return base ** exponent

# Main code
if __name__ == "__main__":
    # Input from the user
    base = float(input("Enter the base number: "))
    exponent = int(input("Enter the exponent: "))
    
    # Call the function and display the result
    result = calculate_power(base, exponent)
    print(f"{base} raised to the power of {exponent} is {result}")
