/**
 * File: RecursiveIntegerApp.cpp
 * Author: Prof. Cristian M. Pagan
 * Course: COSC 240 - Computer Science Programming II
 * Date: 6-noviembre-2026
 * Description: Demuestra el uso de funciones recursivas
 * para calcular el factorial de un número entero.
 */

#include "RecursiveIntArray.h"
#include <iostream>

using namespace std;

// Función principal del programa.
int main()
{
    try
    {
        int arr[] = { 4, 9, 15, 2, 7 };
        int size = sizeof(arr) / sizeof(arr[0]);

        cout << "Elemento maximo: ";
        cout << RecursiveIntArray::maximum(arr, size);
    }
    catch (invalid_argument& err)
    {
        // Captura el error si el argumento no es válido
        cout << err.what();
    }

    return 0;
}