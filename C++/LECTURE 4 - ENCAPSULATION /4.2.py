🔷 Objective:
This program shows how to define and use a class called `employee` that holds employee details.

🔷 Approach:
1. Define private members: `name`, `age`, and `salary`.
2. Use public methods `set_values` and `printdetails` for interaction.
3. Use the `this` pointer to assign values to the object's own members.
4. Print the memory address of the object using both `this` and `&object`.
5. Demonstrates abstraction by exposing only essential interfaces.

🔷 OOP Concepts Used:
- ✅ Encapsulation (private data)
- ✅ Abstraction (public interface)
- ✅ this Pointer (to resolve naming ambiguity)
- ✅ Memory Address Access (this and &object)
- ✅ Classes and Objects


#include <iostream>
using namespace std;

class employee {
private:
    string name;  // ✅ Encapsulation
    int age;      // ✅ Encapsulation
    int salary;   // ✅ Encapsulation

public:
    void set_values(string name, int age, int salary) {
        this->name = name;     // ✅ this Pointer
        this->age = age;
        this->salary = salary;
    }

    void printdetails() {
        cout << "Name: " << name << "\n";     // ✅ Abstraction
        cout << "Age: " << age << "\n";
        cout << "Salary: " << salary << " rupees\n";
        cout << "Object Address (this): " << this << "\n"; // ✅ Memory Address
    }
};

int main() {
    employee e1;   // ✅ Object creation
    e1.set_values("John Bennet", 21, 25000);
    e1.printdetails();
    cout << "Address from outside: " << &e1 << "\n"; // ✅ Memory Address

    employee e2;
    e2.set_values("Jonny Sins", 40, 400000);
    e2.printdetails();
    cout << "Address from outside: " << &e2 << "\n";

    return 0;
}
