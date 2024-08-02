# Function to calculate the perimeter of a rectangle
def calculate_perimeter_of_rectangle(length, width):
    perimeter = 2 * (length + width)
    return perimeter

# Take the length and width as input from the user
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculate the perimeter of the rectangle
perimeter = calculate_perimeter_of_rectangle(length, width)

# Print the result
print(f"The perimeter of the rectangle with length {length} and width {width} is: {perimeter}")
