/*
* File: odd_numbers_for_version.cpp
* Author: Cristian M. Pagan
* Course: COSC 131 - Programming Logic
* Date: September 27, 2026
* Description: Este programa utiliza un ciclo for 
* para mostrar los números impares desde 1 hasta 19.
*/

#include <iostream>

using namespace std;

// Inicia la ejecución del programa.
int main()
{
    // El ciclo comienza en 1, continúa hasta 19
    for (int numero = 1; numero < 20; numero += 2)
    {
        // Muestra el número impar.
        cout << numero << endl;
    }

    // Indica que el programa terminó correctamente.
    return 0;
}
