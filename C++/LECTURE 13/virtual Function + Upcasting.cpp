#include <iostream>
using namespace std;

class Base {
public:
    virtual void show() {
        cout << "Base class show()" << endl;
    }
};

class Derived : public Base {
public:
    void show() override {
        cout << "Derived class show()" << endl;
    }
};

int main() {
    Derived d;           // Create derived class object
    Base* ptr = &d;      // Upcasting: base class pointer points to derived object

    ptr->show();         // Will call Derived class show() because 'show' is virtual

    return 0;
}
