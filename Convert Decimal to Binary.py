# Function to convert decimal to binary
def decimal_to_binary(n):
    # Check if the number is zero
    if n == 0:
        return "0"
    binary = ""
    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n = n // 2
    return binary

# Input from the user
decimal_number = float(input("Enter a decimal number: "))

# Convert to binary
binary_number = decimal_to_binary(decimal_number)

# Output the result
print(f"The binary representation of {decimal_number} is {binary_number}")
