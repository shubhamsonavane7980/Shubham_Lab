with open("myfile.txt", "r") as file:
    content = file.read()

# Transform the content by writing each word on a separate line
transformed_content = "\n".join(content.split())

# Write the transformed content back to the file
with open("myfile.txt", "w") as file:
    file.write(transformed_content)