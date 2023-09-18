import threading

def calculate_square(number):
    result = number ** 2
    print(f"Square of {number} is {result}.")

def calculate_cube(number):
    result = number ** 3
    print(f"Cube of {number} is {result}.")

# Number for calculation
number = 5

# Create two threads
square_thread = threading.Thread(target=calculate_square, args=(number,))
cube_thread = threading.Thread(target=calculate_cube, args=(number,))

# Start the threads
square_thread.start()
cube_thread.start()

# Wait for both threads to complete
square_thread.join()
cube_thread.join()