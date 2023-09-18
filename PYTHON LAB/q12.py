class Vehicle:
    def __init__(self, make, model, seating_capacity):
        self.make = make
        self.model = model
        self.seating_capacity = seating_capacity

    def display_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Seating Capacity: {self.seating_capacity}")

    def fare_charge(self):
        return self.seating_capacity * 100


class Bus(Vehicle):
    def fare_charge(self):
        base_fare = super().fare_charge()
        maintenance_charge = base_fare * 0.1
        total_fare = base_fare + maintenance_charge
        return total_fare


# Creating an instance of the Bus class
my_bus = Bus("Volvo", "B7R", 50)

# Accessing the inherited methods from the Vehicle class
my_bus.display_info()

# Calculating the fare charge for the bus
fare = my_bus.fare_charge()
print(f"The fare charge for the bus is: {fare}")