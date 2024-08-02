# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    # Apply the formula to convert Celsius to Fahrenheit
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Take Celsius temperature as input from the user
celsius_temp = float(input("Enter temperature in Celsius: "))

# Convert Celsius to Fahrenheit
fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)

# Print the result
print(f"The temperature in Fahrenheit is: {fahrenheit_temp}")
