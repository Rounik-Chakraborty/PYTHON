import random

# Function to generate a random number within a specified range
def generate_random_number(min_value, max_value):
    return random.randint(min_value, max_value)

# Take the range as input from the user
min_value = int(input("Enter the minimum value: "))
max_value = int(input("Enter the maximum value: "))

# Generate the random number
random_number = generate_random_number(min_value, max_value)

# Print the result
print(f"The random number between {min_value} and {max_value} is: {random_number}")
