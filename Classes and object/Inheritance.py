# Inheritance Example - Child class inherits from parent class

# Parent class
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} is starting...")

# Child class inheriting from Vehicle
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)   # Call parent constructor
        self.model = model

    def drive(self):
        print(f"Driving {self.brand} {self.model}")

# Create Car object which uses Vehicle features
c = Car("Tesla", "Model X")
c.start()   # Method from Vehicle class
c.drive()   # Method from Car class

'''
Output:
Tesla is starting...
Driving Tesla Model X
'''
