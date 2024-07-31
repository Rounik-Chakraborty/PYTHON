# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Function to print prime numbers in an interval
def print_primes_in_interval(lower, upper):
    print(f"Prime numbers between {lower} and {upper} are:")
    for num in range(lower, upper + 1):
        if is_prime(num):
            print(num, end=' ')
    print()  # for newline

# Input for lower and upper bounds of the interval
lower = int(input("Enter the lower bound of the interval: "))
upper = int(input("Enter the upper bound of the interval: "))

# Function call to print prime numbers
print_primes_in_interval(lower, upper)
