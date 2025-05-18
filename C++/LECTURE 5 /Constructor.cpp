#include <iostream>
using namespace std;

class Points {
    int x;
    int y;

public:
    /*
    Concept: Constructor and 'this' Pointer
    ---------------------------------------
    A constructor is a special function that initializes objects of a class.
    The 'this' pointer is an implicit pointer available in all non-static member functions.
    It points to the current object invoking the method.
    */

    // Parameterized constructor using 'this' pointer to resolve naming conflicts
    Points(int a, int b) {
        this->x = a;
        this->y = b;
    }

    // Member function to display values
    void get_details() {
        cout << "X -> " << x << " Y -> " << y << endl;
    }
};

int main() {
    // Creating two objects using the constructor
    Points d(2, 3), f(45, 7);
    d.get_details();
    f.get_details();

    return 0;
}
