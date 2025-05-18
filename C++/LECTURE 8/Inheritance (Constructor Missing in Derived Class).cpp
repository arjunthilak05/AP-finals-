#include <iostream>
using namespace std;

// Base class
class mathematics {
    int x;         // Private variables
    int y;
    int result;

public:
    // Parameterized constructor
    mathematics(int a, int b) {
        this->x = a;
        this->y = b;
    }

    // Function to compute sum of squares
    void get_square(int a, int b) {
        this->result = a * a + b * b;  // a² + b²
        cout << "Square of two numbers is: " << result << endl;
    }
};

// Derived class using public inheritance
class physics : public mathematics {
public:
    // Derived class must explicitly call base class constructor
    physics(int a, int b) : mathematics(a, b) {
        // Constructor of base class is invoked using initialization list
    }

    // You can extend or override functionality here
    void calculate_squares(int a, int b) {
        get_square(a, b);  // Call base class function
    }
};

int main() {
    // Create object of derived class
    physics p1(3, 4);
    p1.calculate_squares(3, 4);  // Output: 9 + 16 = 25

    return 0;
}
