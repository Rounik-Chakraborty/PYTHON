# Function to find the largest of three numbers
def find_largest(num1, num2, num3):
    if (num1 >= num2) and (num1 >= num3):
        largest = num1
    elif (num2 >= num1) and (num2 >= num3):
        largest = num2
    else:
        largest = num3
    return largest

# Input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Finding the largest number
largest = find_largest(num1, num2, num3)

# Displaying the result
print("The largest number is:", largest)
