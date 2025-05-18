#include <iostream>
#include <string>
#include <cmath>
using namespace std;

class complex {
    double a;
    double b;

public:
    // Constructor
    complex(double a, double b) {
        this->a = a;
        this->b = b;
    }

    // Displays the complex number
    void show_data() {
        cout << "a + ib = " << a << " + i" << b << endl;
    }

    // Operator Overloading for Addition (+)
    complex operator+(const complex g) {
        complex c(0, 0);
        c.a = a + g.a;
        c.b = b + g.b;
        return c;
    }

    // Operator Overloading for Multiplication (*)
    complex operator*(const complex g) {
        complex c(0, 0);
        c.a = a * g.a;
        c.b = b * g.b;
        return c;
    }

    // Operator Overloading for Greater-than (>)
    // Compares magnitude of two complex numbers
    complex operator>(const complex g) {
        double mag1 = sqrt(pow(a, 2) + pow(b, 2));
        double mag2 = sqrt(pow(g.a, 2) + pow(g.b, 2));

        if (mag1 > mag2) {
            return *this;
        } else {
            return g;
        }
    }
};

int main() {
    complex c1(4.6, 4), c2(9, 5.5), c3(0, 0);

    c1.show_data();           // Displays c1
    c3 = c1 + c2;             // Adds two complex numbers
    c3.show_data();           // Displays result

    c3 = c1 * c2;             // Multiplies two complex numbers
    c3.show_data();

    complex c4 = c1 > c2;     // Compares magnitudes
    c4.show_data();           // Displays the larger one

    return 0;
}
