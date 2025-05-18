#include<iostream>
using namespace std;

class Polynomial {
    // Private data members representing coefficients of the polynomial ax^2 + bx + c
    double a;
    double b;
    double c;

public:
    // Static data member to track number of Polynomial objects created
    static int count;

    // Parameterized Constructor - takes 3 integer arguments
    Polynomial(int a, int b, int c) {
        this->a = a;
        this->b = b;
        this->c = c;
        count++; // Increment object count
    }

    // Overloaded Constructor - takes 2 integer arguments, sets c = 0
    Polynomial(int a, int b) {
        this->a = a;
        this->b = b;
        this->c = 0;
        count--; // Decrement object count just to show use of static variable
    }

    // Overloaded Constructor - takes 3 double arguments
    Polynomial(double a, double b, double c) {
        this->a = a;
        this->b = b;
        this->c = c;
        count++;
    }

    // Default Constructor
    Polynomial() {
        // Values not initialized
        count++; // Increase object count
    }

    // Copy Constructor
    Polynomial(Polynomial& object) {
        a = object.a;
        b = object.b;
        c = object.c;
        // Note: static count is not changed in copy constructor
    }

    // Destructor
    ~Polynomial() {
        cout << "Destructor has been called." << endl;
    }

    // Member function to set values
    void set_value(int a, int b, int c) {
        this->a = a;
        this->b = b;
        this->c = c;
    }

    // Member function to display the polynomial
    void get_value() {
        cout << "Polynomial: " << a << "x^2 + " << b << "x + " << c
             << " | Current object count: " << count << endl;
    }
};

// Initialize the static member
int Polynomial::count = 0;

int main() {
    // Object created using 2-parameter constructor (count decreases)
    Polynomial p5(2, 3);
    p5.get_value();

    // Begin block scope to demonstrate destructor
    {
        Polynomial p1(p5);         // Copy constructor
        p1.get_value();

        Polynomial p2(5, 6);       // 2-parameter constructor
        p2.get_value();

        Polynomial p3(3, 4, 5);    // 3-parameter constructor
        p3.get_value();

        Polynomial p4;            // Default constructor
        p4.set_value(1, 2, 3);
        p4.get_value();
    } // All p1 to p4 go out of scope here and destructors are called

    return 0;
}
