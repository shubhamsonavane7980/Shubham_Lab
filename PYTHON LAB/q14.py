import re

def match_string(input_string):
    pattern = r'^[a-zA-Z0-9_]+$'
    if re.match(pattern, input_string):
        return True
    else:
        return False

# Test cases
strings = [
    "Hello_World123",
    "hello_world",
    "Hello123",
    "123456",
    "hello world",
    "Hello-World",
    "Hello_World!",
    "HELLO_WORLD"
]

for string in strings:
    if match_string(string):
        print(f"'{string}' matches the pattern.")
    else:
        print(f"'{string}' does not match the pattern.")