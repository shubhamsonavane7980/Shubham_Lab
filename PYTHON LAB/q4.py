# Accept a sentence from the user
sentence = input("Enter a sentence: ")

# Initialize count variables for letters and digits
letter_count = 0
digit_count = 0

# Iterate through each character in the sentence
for char in sentence:
    # Check if the character is a letter
    if char.isalpha():
        letter_count += 1
    # Check if the character is a digit
    elif char.isdigit():
        digit_count += 1

# Print the count of letters and digits
print("ALPHABETS", letter_count, "DIGITS", digit_count)