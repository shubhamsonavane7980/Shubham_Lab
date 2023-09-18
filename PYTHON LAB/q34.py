from pymongo import MongoClient

# Establish a connection with the MongoDB server
client = MongoClient("mongodb://localhost:27017/")

# Access the book database
database = client["bookdb"]

# Access the books collection
collection = database["books"]

# Function to add a book to the database
def add_book():
    book_id = input("Enter Book ID: ")
    book_name = input("Enter Book Name: ")
    book_author = input("Enter Book Author: ")

    book = {
        "Book_id": book_id,
        "Book_name": book_name,
        "Book_author": book_author
    }

    collection.insert_one(book)
    print("Book added successfully!")

# Function to display all books in the database
def display_books():
    books = collection.find()
    for book in books:
        print(book)

# Function to search for a book by its name
def search_book():
    book_name = input("Enter Book Name to search: ")
    query = {"Book_name": book_name}
    book = collection.find_one(query)
    if book:
        print(book)
    else:
        print("Book not found!")

# Function to sort books by book name
def sort_books():
    books = collection.find().sort("Book_name")
    for book in books:
        print(book)

# Menu-driven program loop
while True:
    print("\nBOOK DATABASE MENU:")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Sort Books")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_book()
    elif choice == "2":
        display_books()
    elif choice == "3":
        search_book()
    elif choice == "4":
        sort_books()
    elif choice == "5":
        break
    else:
        print("Invalid choice! Please try again.")

# Close the MongoDB connection
client.close()