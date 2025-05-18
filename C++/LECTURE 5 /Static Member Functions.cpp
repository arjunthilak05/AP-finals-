#include<iostream>
using namespace std;

class Distance_fi {
private:
    int feet;
    int inch;

public:
    static int count;

    void set_values(int x, int y) {
        this->feet = x;
        this->inch = y;
        count++;  // Track number of set_values() calls
    }

    void get_values() {
        cout << "feet -> " << feet << "\n";
        cout << "inch -> " << inch << "\n" << endl;
    }

    /*
    Concept: Static Member Functions
    ---------------------------------
    - A static function can be called without an object.
    - It only has access to static data members.
    - Useful for utility-like access to class-level data.
    */
    static void count_access() {
        cout << "The value of count is " << count << endl;
    }
};

int Distance_fi::count = 0;

int main() {
    Distance_fi d1, d2;
    d1.set_values(4, 5);
    d1.get_values();
    d2.set_values(5, 5);
    d2.get_values();

    // Accessing static function without object
    Distance_fi::count_access();

    return 0;
}
