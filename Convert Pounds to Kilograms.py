# Function to convert pounds to kilograms
def convert_pounds_to_kilograms(pounds):
    kilograms = pounds * 0.453592
    return kilograms

# Take pounds as input from the user
pounds = float(input("Enter the weight in pounds: "))

# Convert pounds to kilograms
kilograms = convert_pounds_to_kilograms(pounds)

# Print the result
print(f"{pounds} pounds is equal to {kilograms} kilograms.")
