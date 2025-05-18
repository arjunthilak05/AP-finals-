#include <iostream>
#include <string>
using namespace std;

class vector; // Forward declaration

class matrix {
    int arr[2][2];

public:
    matrix(int a, int b, int c, int d) {
        arr[0][0] = a;
        arr[0][1] = b;
        arr[1][0] = c;
        arr[1][1] = d;
    }

    // Declare friend function for matrix-vector multiplication
    friend vector product(matrix* m, vector* v);
};

class vector {
    int arr1[2];

public:
    vector(int a, int b) {
        arr1[0] = a;
        arr1[1] = b;
    }

    void show_data() {
        cout << "Vector Result: " << arr1[0] << " and " << arr1[1] << endl;
    }

    friend vector product(matrix* m, vector* v);
};

// Friend function: not a member of either class but has access to private members
vector product(matrix* m, vector* v) {
    vector t(0, 0);
    t.arr1[0] = m->arr[0][0] * v->arr1[0] + m->arr[0][1] * v->arr1[1];
    t.arr1[1] = m->arr[1][0] * v->arr1[0] + m->arr[1][1] * v->arr1[1];
    return t;
}

int main() {
    matrix m1(1, 2, 3, 4);
    vector v1(1, 2), v4(0, 0);

    // Matrix-vector product
    v4 = product(&m1, &v1);
    v4.show_data();

    return 0;
}
