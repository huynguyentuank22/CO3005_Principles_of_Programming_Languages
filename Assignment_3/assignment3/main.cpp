#include <iostream>

int main() {
    int a[] = {1,3,5};
    int *p = a, *q = p; // -> a
    a[0]++; // {5,5,6}
    ++*q; // {6,5,6}
    *p++; // {6,5,6} -> p = a+1
    std::cout << a[0] + a[1] + a[2] << std::endl;
}