/*
 * File: even_numbers.cpp
 * Author: Cristian M. Pagan
 * Course: COSC 131 - Programming Logic
 * Date: August 10, 2026
 * Description: Este programa muestra los números 
 * pares del 2 al 10 utilizando un ciclo while.
 */

#include <iostream>

using namespace std;

// Inicia la ejecución del programa.
int main()
{
    // Se declara la variable contador y se inicializa en 2.
    int contador = 2;

    // El ciclo while se ejecuta mientras contador sea menor o igual a 10.
    while (contador <= 10)
    {
        // Muestra el número par actual.
        cout << contador << endl;

        // Aumenta el contador en 2 para obtener el siguiente número par.
        contador += 2;
    }

    // Indica que el programa terminó correctamente.
    return 0;
}
