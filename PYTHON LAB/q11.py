class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")


class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        print(f"The seating capacity of this bus is {capacity}.")


# Creating an instance of the Bus class
my_bus = Bus("Volvo", "B7R")

# Accessing the inherited methods from the Vehicle class
my_bus.display_info()

# Calling the seating_capacity method with default value
my_bus.seating_capacity()

# Calling the seating_capacity method with a custom value
my_bus.seating_capacity(60)