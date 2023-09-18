from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
database = client["student_db"]
collection = database["students"]



def add_student():
    student_id = input("Enter Student ID: ")
    student_name = input("Enter Student Name: ")
    course = input("Enter Course: ")

    student = {
        "student_id": student_id,
        "student_name": student_name,
        "course": course
    }

    collection.insert_one(student)
    print("Student added successfully!")


def display_students():
    students = collection.find()

    for student in students:
        print(f"Student ID: {student['student_id']}")
        print(f"Student Name: {student['student_name']}")
        print(f"Course: {student['course']}")
        print()


def update_student():
    student_id = input("Enter Student ID to update: ")
    new_student_name = input("Enter New Student Name: ")
    new_course = input("Enter New Course: ")

    update_query = {
        "student_id": student_id
    }

    new_values = {
        "$set": {
            "student_name": new_student_name,
            "course": new_course
        }
    }

    collection.update_one(update_query, new_values)
    print("Student updated successfully!")


def delete_student():
    student_id = input("Enter Student ID to delete: ")

    delete_query = {
        "student_id": student_id
    }

    collection.delete_one(delete_query)
    print("Student deleted successfully!")

while True:
    print("Student Database Menu:")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        break
    else:
        print("Invalid choice! Please try again.")

    print()

if __name__ == "__main__":
    print("Welcome to Student Database!")
    print("-----------------------------")
    print()

    while True:
        username = input("Enter MongoDB username: ")
        password = input("Enter MongoDB password: ")

        try:
            client = MongoClient(f"mongodb+srv://{username}:{password}@cluster0.mongodb.net/")
            database = client["student_db"]
            collection = database["students"]
            break
        except:
            print("Connection failed! Please try again.")

    print("Connection successful!")
    print()

    # Run the main menu loop
    while True:
        print("Student Database Menu:")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            break
        else:
            print("Invalid choice! Please try again.")

        print()