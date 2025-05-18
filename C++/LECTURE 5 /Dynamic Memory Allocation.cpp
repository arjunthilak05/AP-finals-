#include <iostream>
using namespace std;

int main() {
    /*
    Concept: Dynamic Memory Allocation
    -----------------------------------
    In C++, dynamic memory can be allocated using the 'new' keyword.
    The 'new' operator allocates memory at runtime from the heap.
    This is useful when the size of an array or object is not known at compile time.
    Remember to free dynamically allocated memory using 'delete' or 'delete[]' to prevent memory leaks.
    */

    // Dynamically allocating memory for an integer array of size 5
    int* arr = new int[5];

    // Taking input into dynamically allocated array
    for (int i = 0; i < 5; i++) {
        cout << "Enter the value: ";
        cin >> arr[i];
    }

    // Outputting the contents of the array
    for (int j = 0; j < 5; j++) {
        cout << arr[j] << " ";
    }

    // Freeing the allocated memory
    delete[] arr;

    return 0;
}
