# Accept number from the user
X = int(input("Enter a number: "))

# Calculate the number of digits in the number
num_digits = len(str(X))

# Initialize the sum variable
sum = 0

# Temporary variable to store the original number
temp = X

# Calculate the sum of cubes of each digit
while temp > 0:
    digit = temp % 10
    sum += digit ** num_digits
    temp //= 10

# Check if the number is an Armstrong number
if X == sum:
    print(X, "is an Armstrong number.")
else:
    print(X, "is not an Armstrong number.")