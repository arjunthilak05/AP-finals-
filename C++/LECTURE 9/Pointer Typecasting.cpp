#include <iostream>
using namespace std;

int main() {
    int i = 1;
    int* a = &i;

    double s = 5.2;
    double* b = &s;

    // Typecasting pointers
    a = (int*)b;     // forcibly treat double* as int*
    b = (double*)a;  // and vice versa

    // Warning: Dangerous and non-portable! This can cause memory access issues

    return 0;
}
