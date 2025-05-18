#include<iostream>
using namespace std;

class Polynomial {
private:
    int a, b, c;  // Coefficients for ax^2 + bx + c

public:
    void set_values(int x, int y, int z) {
        this->a = x;
        this->b = y;
        this->c = z;
    }

    void get_values() {
        cout << "Polynomial: " << a << "x^2 + " << b << "x + " << c << endl;
    }

    /*
    Concept: Object-Oriented Representation of Mathematical Concepts
    ----------------------------------------------------------------
    - Encapsulation helps group data (coefficients) and functionality (addition).
    - Object interaction enables combining two polynomials inside a third.
    */
    void add_polynomials(Polynomial p1, Polynomial p2) {
        this->a = p1.a + p2.a;
        this->b = p1.b + p2.b;
        this->c = p1.c + p2.c;
    }
};

int main() {
    Polynomial p1, p2, sum;
    p1.set_values(5, 4, 2);
    p2.set_values(3, 10, 1);
    p1.get_values();
    p2.get_values();

    // Performing polynomial addition using member function
    sum.add_polynomials(p1, p2);
    sum.get_values();

    return 0;
}
