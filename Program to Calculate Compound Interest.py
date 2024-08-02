# Function to calculate compound interest
def calculate_compound_interest(principal, rate, time):
    amount = principal * (1 + rate / 100) ** time
    compound_interest = amount - principal
    return compound_interest

# Take principal, rate, and time as inputs from the user
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in %): "))
time = float(input("Enter the time (in years): "))

# Calculate the compound interest
compound_interest = calculate_compound_interest(principal, rate, time)

# Print the result
print(f"The compound interest for a principal amount of {principal} at a rate of {rate}% for {time} years is: {compound_interest}")
