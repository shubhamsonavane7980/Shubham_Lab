def extract_lines(file_path, start_line, end_line, output_file):
    with open(file_path, 'r') as file:
        lines = file.readlines()

        # Adjust start and end line indices to account for zero-based indexing
        start_line -= 1
        end_line -= 1

        # Ensure start_line and end_line are within valid range
        start_line = max(0, start_line)
        end_line = min(len(lines) - 1, end_line)

        # Extract the desired lines
        extracted_lines = lines[start_line:end_line+1]

    # Write the extracted lines to the output file
    with open(output_file, 'w') as output:
        output.writelines(extracted_lines)

# Path to the input file
input_file_path = 'myfile.txt'

# Line range to extract
start_line = 3
end_line = 7

# Path to the output file
output_file_path = 'extract_content.txt'

# Extract the lines and save them to the output file
extract_lines(input_file_path, start_line, end_line, output_file_path)

print(f"Lines {start_line} to {end_line} extracted and saved to {output_file_path}.")