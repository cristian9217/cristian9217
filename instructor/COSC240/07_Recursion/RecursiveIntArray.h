/**
 * File: RecursiveIntegerArray.cpp
 * Author: Prof. Cristian M. Pagan
 * Course: COSC 240 - Computer Science Programming II
 * Date: 6-noviembre-2026
 * Description: Demuestra el uso de funciones recursivas
 * para calcular el maximo elemento de un arreglo.
 */

#include <iostream>

using namespace std;

class RecursiveIntArray
{
    private:
        /**
         * Returns the maximum element of the specified array.
         * @param arr The array to be processed.
         * @param len The length of the array.
         * @return The maximum element.
         */
        static int maximumHelper(int arr[], int size) {
            if (size == 1)
                return arr[0];
            else
                return max(maximumHelper(arr, size - 1), arr[size - 1]);
        }
    
    public:
        /**
         * Returns the maximum element of the specified array.
         * @param arr The array to be processed.
         * @param size The number of elements in the array.
         * @throws invalid_argument if the array is empty.
         */
        static int maximum(int arr[], int size) {
            if (size == 0)
                throw invalid_argument("empty array");

            return maximumHelper(arr, size);
        }
};
        


        