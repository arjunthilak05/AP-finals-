# Constructor Example - Automatically initializes object with given values

class Employee:
    # Constructor method is defined using __init__
    def __init__(self, name, role, salary):
        self.name = name          # Set name attribute
        self.role = role          # Set role attribute
        self.salary = salary      # Set salary attribute
        print(f"{self.name} created with role {self.role} and salary ₹{self.salary}")

    # A method to show employee details
    def show(self):
        print(f"Name: {self.name}, Role: {self.role}, Salary: ₹{self.salary}")

# Creating objects with initial values using constructor
e1 = Employee("Arjun", "Developer", 70000)
e2 = Employee("Ram", "Manager", 90000)

# Displaying employee details
e1.show()
e2.show()

'''
Output:
Arjun created with role Developer and salary ₹70000
Ram created with role Manager and salary ₹90000
Name: Arjun, Role: Developer, Salary: ₹70000
Name: Ram, Role: Manager, Salary: ₹90000
'''
