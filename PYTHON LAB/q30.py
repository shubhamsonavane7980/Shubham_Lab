import numpy as np

# Create a 3x3 NumPy array with user input
array = np.zeros((3, 3))

for i in range(3):
    for j in range(3):
        num = int(input(f"Enter element at position ({i}, {j}): "))
        array[i, j] = num

# Calculate the sum of all elements in the array
array_sum = np.sum(array)

# Print the array and the sum
print("Array:")
print(array)
print("Sum of all elements:", array_sum)