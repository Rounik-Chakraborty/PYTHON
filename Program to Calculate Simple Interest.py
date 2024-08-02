# Function to calculate simple interest
def calculate_simple_interest(principal, rate, time):
    simple_interest = (principal * rate * time) / 100
    return simple_interest

# Take principal, rate, and time as inputs from the user
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time (in years): "))

# Calculate the simple interest
simple_interest = calculate_simple_interest(principal, rate, time)

# Print the result
print(f"The simple interest for a principal amount of {principal} at a rate of {rate}% for {time} years is: {simple_interest}")
