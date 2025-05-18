#include<iostream>
using namespace std;

class Distance_fi {
private:
    int feet;
    int inch;

public:
    static int count;  // Static data member shared by all instances

    /*
    Concept: Static Members
    ------------------------
    - Static members are shared across all instances of the class.
    - They are used for class-level data like counters, flags, etc.
    */

    void set_values(int x, int y) {
        this->feet = x;
        this->inch = y;
        count++;  // Count how many times this function is called
    }

    void get_values() {
        cout << "feet -> " << feet << "\n";
        cout << "inch -> " << inch << "\n" << endl;
    }

    /*
    Concept: Friend Functions
    --------------------------
    - Friend functions are not members of a class but can access private and protected members.
    - Useful for operations involving multiple objects (e.g., operator overloading, arithmetic).
    */
    friend Distance_fi Sum_function(Distance_fi d1, Distance_fi d2);

    static void count_access() {
        // Static member function can access only static data members
        cout << "The value of count is " << count << endl;
    }
};

// Friend function definition outside class
Distance_fi Sum_function(Distance_fi c1, Distance_fi c2) {
    Distance_fi d4;
    d4.feet = c1.feet + c2.feet;
    d4.inch = c1.inch + c2.inch;
    if (d4.inch >= 12) {
        d4.feet += d4.inch / 12;
        d4.inch = d4.inch % 12;
    }
    return d4;
}

// Initialization of static member
int Distance_fi::count = 0;

int main() {
    Distance_fi d1, d2, sum;
    d1.set_values(4, 5);
    d1.get_values();
    d2.set_values(5, 100);
    d2.get_values();

    Distance_fi::count_access();  // Static function call without object

    sum = Sum_function(d1, d2);   // Friend function used to add two objects
    sum.get_values();

    Distance_fi::count_access();

    return 0;
}

