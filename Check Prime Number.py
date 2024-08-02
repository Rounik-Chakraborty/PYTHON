def is_prime(n):
    # Check if number is less than or equal to 1
    if n <= 1:
        return False
    # Check from 2 to n-1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Take input from the user
number = int(input("Enter a number: "))

# Check if the number is prime
if is_prime(number):
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")
