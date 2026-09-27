/*
* File: squares.cpp
* Author: Cristian M. Pagan
* Course: COSC 131 - Programming Logic
* Date: September 27, 2026
* Description: Este programa solicita un número entero 
* limit y utiliza un ciclo for para mostrar el cuadrado 
* de cada número desde 1 hasta limit.
*/

#include <iostream>

using namespace std;

// Inicia la ejecución del programa.
int main()
{
    // Declara la variable para almacenar N.
    int limit;

    // Solicita el número al usuario.
    cout << "Ingrese un numero entero: ";
    cin >> limit;

    // Recorre los números desde 1 hasta N.
    for (int numero = 1; numero <= limit; numero++)
    {
        // Muestra el número y su cuadrado.
        cout << numero << "^2" << " = " << numero * numero << endl;
    }

    // Indica que el programa terminó correctamente.
    return 0;
}
