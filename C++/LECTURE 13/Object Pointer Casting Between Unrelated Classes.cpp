#include <iostream>
using namespace std;

class A {
public:
    int a;
};

class B {
public:
    int b;
};

int main() {
    A* oa;
    B* ob;

    // oa = ob; // ❌ Implicit casting not allowed between unrelated classes

    oa = (A*)ob; // ✅ Explicit casting, but still unsafe

    oa->a = 4; // ☠️ Might overwrite memory, dangerous if B doesn't actually contain `int a`
    cout << "Value of a: " << oa->a << endl;

    return 0;
}
