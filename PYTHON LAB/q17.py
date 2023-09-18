import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    else:
        return False

# Test cases
emails = [
    "john.doe@example.com",
    "jane_smith@example.co.uk",
    "test123@example",
    "invalid.email@",
    "user@example_com",
    "user@.com",
    "user@example..com",
    "user@-example.com",
    "user@example+domain.com"
]

for email in emails:
    if validate_email(email):
        print(f"'{email}' is a valid email address.")
    else:
        print(f"'{email}' is not a valid email address.")