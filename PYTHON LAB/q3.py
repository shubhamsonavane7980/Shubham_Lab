# Initialize an empty list to store the numbers
even_numbers = []

# Iterate through numbers from 2000 to 3000 (both inclusive)
for num in range(2000, 3001):
    # Convert the number to a string
    num_str = str(num)
    
    # Flag to keep track if all digits are even
    all_even = True
    
    # Check if each digit is even
    for digit in num_str:
        if int(digit) % 2 != 0:
            all_even = False
            break
    
    # If all digits are even, add the number to the list
    if all_even:
        even_numbers.append(num)

# Print the numbers with all even digits
print("Numbers with all even digits between 2000 and 3000:")
print(even_numbers)