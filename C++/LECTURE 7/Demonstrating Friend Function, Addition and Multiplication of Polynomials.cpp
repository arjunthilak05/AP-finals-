#include<iostream>
using namespace std;

class Polynomial {
private:
    int a, b, c; // Coefficients of polynomial ax^2 + bx + c

public:
    // Set values using this pointer
    void set_values(int x, int y, int z) {
        this->a = x;
        this->b = y;
        this->c = z;
    }

    // Display polynomial
    void get_values() {
        cout << "Polynomial: " << a << "x^2 + " << b << "x + " << c << endl;
    }

    // Member function to add two polynomials
    void add_polynomials(Polynomial p1, Polynomial p2) {
        this->a = p1.a + p2.a;
        this->b = p1.b + p2.b;
        this->c = p1.c + p2.c;
    }

    // Declare friend function to multiply polynomials
    friend Polynomial mul_polynomial(Polynomial p1, Polynomial p2);
};

// Friend function can access private members of both objects
Polynomial mul_polynomial(Polynomial p1, Polynomial p2) {
    Polynomial result;

    // Multiply the polynomials and store in result
    // Only handles specific terms; not general polynomial multiplication
    result.c = p1.c * p2.c;
    result.b = (p1.b * p2.c) + (p1.c * p2.b);
    result.a = p1.b * p2.b;

    return result;
}

int main() {
    Polynomial p1, p2, sum, product;

    // Set values for p1 and p2
    p1.set_values(0, 3, 4); // 3x + 4
    p2.set_values(0, 1, 4); // x + 4

    // Display input polynomials
    p1.get_values();
    p2.get_values();

    // Add the polynomials using member function
    sum.add_polynomials(p1, p2);
    cout << "After Addition: ";
    sum.get_values();

    // Multiply polynomials using friend function
    product = mul_polynomial(p1, p2);
    cout << "After Multiplication (partial): ";
    product.get_values();

    return 0;
}
