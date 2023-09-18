class AgeBelow18Error(Exception):
    def __init__(self, message="Age is below 18 years."):
        self.message = message
        super().__init__(self.message)

def validate_age(age):
    if age < 18:
        raise AgeBelow18Error()

try:
    age = int(input("Enter your age: "))
    validate_age(age)
    print("Age is valid.")
except AgeBelow18Error as e:
    print(f"Error: {str(e)}")
except ValueError:
    print("Error: Invalid input. Please enter a valid age.")