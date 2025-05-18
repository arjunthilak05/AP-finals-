#include <iostream>
using namespace std;

int main() {
    int i = 2;
    double j = 3;
    int* iptr = &i;
    double* jptr = &j;

    // iptr = jptr; // ❌ Invalid: implicit casting not allowed between incompatible pointer types

    iptr = (int*)jptr;    // ✅ Explicitly cast double* to int* (DANGEROUS: type mismatch)
    jptr = (double*)iptr; // ✅ Explicitly cast int* to double*

    return 0;
}
