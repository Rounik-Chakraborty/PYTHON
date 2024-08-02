# Function to print multiplication table of a given number
def print_multiplication_table(number, limit):
    print(f"Multiplication table for {number}:")
    for i in range(1, limit + 1):
        print(f"{number} x {i} = {number * i}")

# Main code
if __name__ == "__main__":
    # Input from the user
    num = int(input("Enter the number for the multiplication table: "))
    limit = int(input("Enter the limit up to which you want the table: "))
    
    # Call the function to print the multiplication table
    print_multiplication_table(num, limit)

