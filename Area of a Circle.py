import math

# Function to calculate the area of a circle
def calculate_area_of_circle(radius):
    area = math.pi * radius ** 2
    return area

# Take the radius as input from the user
radius = float(input("Enter the radius of the circle: "))

# Calculate the area of the circle
area = calculate_area_of_circle(radius)

# Print the result
print(f"The area of the circle with radius {radius} is: {area}")
