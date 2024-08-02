#1.USING FORMULA

def sum_of_natural_numbers(n):
    # Using the formula
    return n * (n + 1) // 2

# Example usage
n = int(input("Enter a positive integer: "))
if n > 0:
    print(f"The sum of natural numbers up to {n} is: {sum_of_natural_numbers(n)}")
else:
    print("Please enter a positive integer.")



'''
2. WITH LOOP

def sum_of_natural_numbers(n):
    # Using a loop
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += i
    return total_sum

# Example usage
n = int(input("Enter a positive integer: "))
if n > 0:
    print(f"The sum of natural numbers up to {n} is: {sum_of_natural_numbers(n)}")
else:
    print("Please enter a positive integer.")
'''