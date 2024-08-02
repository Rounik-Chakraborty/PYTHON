import string

def remove_punctuation(input_string):
    # Create a translation table for removing punctuation
    translator = str.maketrans('', '', string.punctuation)
    
    # Use the translate method to remove punctuation
    return input_string.translate(translator)

# Example usage
input_string = "Hello, world! This is a test string with punctuation."
clean_string = remove_punctuation(input_string)

print("Original String: ", input_string)
print("String without Punctuation: ", clean_string)
