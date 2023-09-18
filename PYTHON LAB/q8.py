def table_generator(number, limit):
    current = 1
    while current <= limit:
        yield number * current
        current += 1

# Test the generator function
number = int(input("Enter a number: "))
limit = int(input("Enter the limit: "))

table = table_generator(number, limit)

print(f"Table of {number} up to {limit}:")
for value in table:
    print(value)
