/**
 * File: RecursiveIntegerApp.cpp
 * Author: Prof. Cristian M. Pagan
 * Course: COSC 240 - Computer Science Programming II
 * Date: 6-noviembre-2026
 * Description: Demuestra el uso de funciones recursivas
 * para calcular el factorial de un número entero.
 */

#include "RecursiveInteger.h"
#include <iostream>

using namespace std;

// Función principal del programa.
int main()
{
    try
    {
        // Intenta calcular e imprimir el factorial de 5.
        cout << "Factorial de 5: ";
        cout << RecursiveInteger::factorial(5) << endl;

        cout << "Fibonacci del 1 al 5:" << endl;
        for (int idx = 1; idx < 6; idx++) 
        {
            cout << RecursiveInteger::fibonacci(idx) << endl;
        }
    }
    catch (invalid_argument& err)
    {
        // Captura el error si el argumento no es válido
        cout << err.what();
    }

    return 0;
}