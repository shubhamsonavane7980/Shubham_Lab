class Student:
    def __init__(self, student_name, marks):
        self.student_name = student_name
        self.marks = marks

# Creating an instance of the Student class
student = Student("John Doe", 85)

# Printing the original attribute values
print("Original values:")
print(f"Student Name: {student.student_name}")
print(f"Marks: {student.marks}")

# Modifying the attribute values
student.student_name = "Jane Smith"
student.marks = 92

# Printing the modified attribute values
print("\nModified values:")
print(f"Student Name: {student.student_name}")
print(f"Marks: {student.marks}")