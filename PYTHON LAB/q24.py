def find_longest_word(file_path):
    longest_word = ''
    
    with open(file_path, 'r') as file:
        content = file.read()
        words = content.split()
        
        for word in words:
            if len(word) > len(longest_word):
                longest_word = word
    
    return longest_word

# Path to the text file
file_path = 'myfile.txt'

# Find the longest word
longest_word = find_longest_word(file_path)

# Display the longest word
print(f"The longest word in the file is: {longest_word}")