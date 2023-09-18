import numpy as np

# 1D array
arr1 = np.array([1, 2, 3, 4, 5])

# 2D array
arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Addition
addition_1d = arr1 + 10
addition_2d = arr2 + 5

# Subtraction
subtraction_1d = arr1 - 2
subtraction_2d = arr2 - 3

# Multiplication
multiplication_1d = arr1 * 3
multiplication_2d = arr2 * 2

# Division
division_1d = arr1 / 2
division_2d = arr2 / 4

# Print the results
print("1D Array:")
print("Original Array:", arr1)
print("Addition:", addition_1d)
print("Subtraction:", subtraction_1d)
print("Multiplication:", multiplication_1d)
print("Division:", division_1d)

print("\n2D Array:")
print("Original Array:")
print(arr2)
print("Addition:")
print(addition_2d)
print("Subtraction:")
print(subtraction_2d)
print("Multiplication:")
print(multiplication_2d)
print("Division:")
print(division_2d)