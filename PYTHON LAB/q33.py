# Import the necessary module
from pymongo import MongoClient

# Establish a connection with the MongoDB server
client = MongoClient("mongodb://localhost:27017/")
# Replace "localhost" with the IP address or hostname of the MongoDB server
# Replace "27017" with the port number where MongoDB is running

# Access a specific database
database = client["mydatabase"]
# Replace "mydatabase" with the name of the database you want to access

# Access a specific collection within the database
collection = database["mycollection"]
# Replace "mycollection" with the name of the collection you want to access

# Perform database operations
# Example: Insert a document into the collection
document = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}
collection.insert_one(document)
# This will insert the document into the specified collection

# Example: Query documents from the collection
query = {"name": "John Doe"}
results = collection.find(query)
for result in results:
    print(result)
# This will find all documents in the collection that match the given query and print them

# Example: Update a document in the collection
filter = {"name": "John Doe"}
update = {"$set": {"age": 35}}
collection.update_one(filter, update)
# This will update the first document in the collection that matches the given filter

# Example: Delete a document from the collection
filter = {"name": "John Doe"}
collection.delete_one(filter)
# This will delete the first document in the collection that matches the given filter

# Close the MongoDB connection
client.close()