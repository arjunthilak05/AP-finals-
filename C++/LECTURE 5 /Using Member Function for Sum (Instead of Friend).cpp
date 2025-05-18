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
        count++;
    }

    void get_values() {
        cout << "feet -> " << feet << "\n";
        cout << "inch -> " << inch << "\n" << endl;
    }

    static void count_access() {
        cout << "The value of count is " << count << endl;
    }

    /*
    Concept: Object Interaction (Member Function)
    ----------------------------------------------
    A member function can take objects as parameters to perform operations between them.
    In this case, it replaces the friend function by directly accessing members.
    */
    void Sum_function(Distance_fi c1, Distance_fi c2) {
        this->feet = c1.feet + c2.feet;
        this->inch = c1.inch + c2.inch;
        if (inch >= 12) {
            this->feet += inch / 12;
            this->inch = inch % 12;
        }
    }
};

int Distance_fi::count = 0;

int main() {
    Distance_fi d1, d2, sum;
    d1.set_values(4, 5);
    d1.get_values();
    d2.set_values(5, 100);
    d2.get_values();

    Distance_fi::count_access();

    // Using member function for sum instead of friend
    sum.Sum_function(d1, d2);
    sum.get_values();

    Distance_fi::count_access();

    return 0;
}
