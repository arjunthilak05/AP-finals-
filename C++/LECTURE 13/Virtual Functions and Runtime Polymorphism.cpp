#include <iostream>
using namespace std;

// Base class
class Animal {
public:
    // Virtual function
    virtual void sound() {
        cout << "Animal makes a sound" << endl;
    }
};

// Derived class
class Dog : public Animal {
public:
    void sound() override {
        cout << "Dog barks" << endl;
    }
};

// Another Derived class
class Cat : public Animal {
public:
    void sound() override {
        cout << "Cat meows" << endl;
    }
};

int main() {
    Animal* a1;        // Base class pointer

    Dog d;
    Cat c;

    a1 = &d;
    a1->sound();       // Output: Dog barks

    a1 = &c;
    a1->sound();       // Output: Cat meows

    return 0;
}
