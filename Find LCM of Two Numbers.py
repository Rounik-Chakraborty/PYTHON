def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    return (x * y) // gcd(x, y)

# Input from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Calculate LCM
result = lcm(num1, num2)

# Display the result
print(f"The LCM of {num1} and {num2} is {result}")
