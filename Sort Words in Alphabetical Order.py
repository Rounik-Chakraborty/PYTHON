# Step 1: Input the string
input_string = input("Enter a string: ")

# Step 2: Split the string into words
words = input_string.split()

# Step 3: Sort the list of words
words.sort()

# Step 4: Join the sorted list back into a string
sorted_string = ' '.join(words)

# Step 5: Print the sorted string
print("Sorted words:", sorted_string)
