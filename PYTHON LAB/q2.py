# Accept string from the user
STR1 = input("Enter a string: ")

# Convert the string to lowercase to handle both uppercase and lowercase vowels
str_lower = STR1.lower()

# Initialize the vowel count variable
count = 0

# Define a list of vowels
vowels = ['a', 'e', 'i', 'o', 'u']

# Count the number of vowels in the string
for char in str_lower:
    if char in vowels:
        count += 1

# Print the count of vowels
print("Number of vowels in the string:", count)