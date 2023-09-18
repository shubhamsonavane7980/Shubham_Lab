def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    elif age > 120:
        raise ValueError("Age cannot be greater than 120.")
    else:
        print("Age is valid.")

# Test cases
try:
    validate_age(25)
    validate_age(-10)
    validate_age(150)
except ValueError as e:
    print(f"Error: {str(e)}")