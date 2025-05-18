#include <iostream>
#include <string>
using namespace std;

// Base class
class employee {
    int id;             // Employee ID
    int salary;         // Employee Salary
    string name;        // Employee Name

public:
    // Constructor with parameters
    employee(int a, int b, string c) {
        this->id = a;           // Using 'this' pointer to refer to current object
        this->salary = b;
        this->name = c;
    }

    // Member function to print employee details
    void get_details() {
        cout << "ID: " << id << " Salary: " << salary << " Name: " << name << endl;
    }

    // Destructor (commented out here but can be used for cleanup or debug)
    // ~employee() {
    //     cout << "Destroyed" << endl;
    // }
};

// Derived class using private inheritance
class engineer : private employee {
public:
    string skill;   // Extra member in derived class

    // Constructor with initialization list to call base class constructor
    engineer(int id, int salary, string name, string skill) : employee(id, salary, name) {
        this->skill = skill;   // Setting own data member
    }

    // Accessing base class function to display info
    void get_2() {
        get_details(); // Accessible because inheritance is within the class
        cout << "Skill: " << skill << endl;
    }
};

int main() {
    // Creating engineer object and calling display function
    engineer e1(1, 90000, "Hari Vishnu", "C++ Expert");
    e1.get_2();  // Prints employee and skill info

    return 0;
}
