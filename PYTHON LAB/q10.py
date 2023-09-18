class Vehicle:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def drive(self):
        print("The vehicle is driving.")

    def stop(self):
        print("The vehicle has stopped.")


class Bus(Vehicle):
    def __init__(self, brand, color, capacity):
        super().__init__(brand, color)
        self.capacity = capacity

    def open_doors(self):
        print("The bus doors are opened.")

    def close_doors(self):
        print("The bus doors are closed.")


# Create an instance of the Bus class
my_bus = Bus("Mercedes", "Blue", 50)

# Access the inherited attributes from the Vehicle class
print("Brand:", my_bus.brand)
print("Color:", my_bus.color)

# Call the inherited methods from the Vehicle class
my_bus.drive()
my_bus.stop()

# Call the methods specific to the Bus class
my_bus.open_doors()
my_bus.close_doors()