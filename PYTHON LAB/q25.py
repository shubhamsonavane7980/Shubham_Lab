def count_word_frequency(file_path):
    word_frequency = {}

    with open(file_path, 'r') as file:
        content = file.read()
        words = content.split()

        for word in words:
            if word in word_frequency:
                word_frequency[word] += 1
            else:
                word_frequency[word] = 1

    return word_frequency

# Path to the text file
file_path = 'myfile.txt'

# Count word frequency
frequency = count_word_frequency(file_path)

# Display the word frequency
for word, count in frequency.items():
    print(f"{word}: {count}")