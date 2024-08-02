# Function to find factors of a number
def find_factors(number):
    factors = []
    # Iterate from 1 to the number itself
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

# Main code
if __name__ == "__main__":
    # Input from the user
    num = int(input("Enter a number: "))
    
    # Call the function and get the factors
    factors = find_factors(num)
    print("The factors of", num, "are:", factors)
