
🔷 Objective:
This program demonstrates key Object-Oriented Programming (OOP) concepts using a class named `student`.

🔷 Approach:
1. Define a class `student` with private data members `marks` and `roll_no`.
2. Use public methods (`set_values`, `get_values`, `squared`) to interact with the class.
3. Demonstrate encapsulation by keeping data and some methods private.
4. Include a private method `greet()` that is only callable from within the class.
5. Use modularity and good design practices to split functionality clearly.
6. Use multiple objects to show instance-based behavior.

🔷 OOP Concepts Used:
- ✅ Encapsulation (private members)
- ✅ Abstraction (public interface, private logic)
- ✅ Private Method (`greet`)
- ✅ Return Function (`squared`)
- ✅ Classes and Objects

🔷 Output:
- Shows how values are stored and accessed using methods.
- Shows result of squaring the values using a member function.

#include <iostream>
using namespace std;

class student {
private:
    int marks;     // ✅ Encapsulation
    int roll_no;   // ✅ Encapsulation

    void greet() { // ✅ Private Method
        cout << "Good morning, your marks is " << marks << ".\n";
    }

public:
    void set_values(int x, int y) { // ✅ Abstraction
        marks = x;
        roll_no = y;
    }

    void get_values() { // ✅ Abstraction
        cout << "The values of variables inside object are: " << marks << " and " << roll_no << "\n";
    }

    int squared() {     // ✅ Abstraction + Return
        greet();        // ✅ Uses private method
        return (marks * marks) + (roll_no * roll_no);
    }
};

int main() {
    student s1;                   // ✅ Object creation
    s1.set_values(2, 3);          // ✅ Method call
    s1.get_values();
    cout << "Sum of squares for s1: " << s1.squared() << "\n";

    student s2;
    s2.set_values(10, 13);
    s2.get_values();
    cout << "Sum of squares for s2: " << s2.squared() << "\n";

    return 0;
}
