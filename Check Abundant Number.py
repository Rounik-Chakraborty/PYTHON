# Function to find the sum of proper divisors of a number
def sum_of_proper_divisors(number):
    total_sum = 0
    # Iterate from 1 to half of the number (since a factor cannot be more than half of the number)
    for i in range(1, number // 2 + 1):
        if number % i == 0:
            total_sum += i
    return total_sum

# Function to check if a number is an abundant number
def is_abundant_number(number):
    # Find the sum of proper divisors
    divisors_sum = sum_of_proper_divisors(number)
    # Check if the sum of proper divisors is greater than the number
    return divisors_sum > number

# Main code
if __name__ == "__main__":
    # Input from the user
    num = int(input("Enter a number: "))
    
    # Call the function and display the result
    if is_abundant_number(num):
        print(num, "is an abundant number.")
    else:
        print(num, "is not an abundant number.")
