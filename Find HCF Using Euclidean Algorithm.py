# Function to find HCF/GCD using Euclidean Algorithm
def find_hcf(a, b):
    # Continue looping until b becomes 0
    while b:
        # Compute the remainder
        a, b = b, a % b
    # Return the HCF/GCD
    return a

# Main code
if __name__ == "__main__":
    # Input from the user
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    
    # Call the function and display the result
    result = find_hcf(num1, num2)
    print("The HCF/GCD of", num1, "and", num2, "is", result)
