#include <iostream>
#include "IntArraySearching.h"

using namespace std;

int main() 
{
    int numbers[] = {10, 20, 30, 40, 50};
    int size = sizeof(numbers) / sizeof(numbers[0]);

    cout << IntArraySearching::sequentialSearch(numbers, size, 30) << endl;
    cout << IntArraySearching::binarySearch(numbers, size, 40) << endl;
    cout << IntArraySearching::binarySearch(numbers, size, 25) << endl;

    return 0;
}
