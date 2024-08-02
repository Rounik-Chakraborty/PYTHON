# Function to convert binary to decimal
def binary_to_decimal(binary):
    # Initialize decimal value
    decimal = 0
    
    # Reverse the binary string to process from right to left
    binary = binary[::-1]
    
    # Traverse the binary string
    for i in range(len(binary)):
        # If the digit is '1', add 2^i to the decimal value
        if binary[i] == '1':
            decimal += 2 ** i
    
    return decimal

# Take binary number as input
binary_number = input("Enter a binary number: ")

# Convert binary to decimal
decimal_number = binary_to_decimal(binary_number)

# Print the result
print(f"The decimal equivalent of binary {binary_number} is {decimal_number}")
