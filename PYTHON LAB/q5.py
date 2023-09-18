def get_unique_elements(input_list):
    # Create an empty list to store unique elements
    unique_list = []

    # Iterate through each element in the input list
    for element in input_list:
        # Check if the element is not already in the unique list
        if element not in unique_list:
            # Add the element to the unique list
            unique_list.append(element)

    # Return the unique list
    return unique_list

# Example usage:
sample_list = [1, 2, 3, 3, 3, 3, 4, 5]
unique_list = get_unique_elements(sample_list)
print("Unique List:", unique_list)