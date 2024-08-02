# Function to convert kilometers to miles
def convert_kilometers_to_miles(kilometers):
    miles = kilometers * 0.621371
    return miles

# Take kilometers as input from the user
kilometers = float(input("Enter the distance in kilometers: "))

# Convert kilometers to miles
miles = convert_kilometers_to_miles(kilometers)

# Print the result
print(f"{kilometers} kilometers is equal to {miles} miles.")
