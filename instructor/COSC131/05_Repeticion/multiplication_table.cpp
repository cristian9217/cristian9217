/*
 * File: multiplication_table.cpp
 * Author: Cristian M. Pagan
 * Course: COSC 131 - Programming Logic
 * Date: August 10, 2026
 * Description: Este programa solicita un número al usuario 
 * y muestra su tabla de multiplicar del 1 al 10 utilizando 
 * un ciclo while.
 */

#include <iostream>

using namespace std;

// Inicia la ejecución del programa.
int main()
{
    // Se declaran las variables para almacenar el número y el contador.
    int numero;
    int contador = 1;

    // Solicita al usuario que ingrese un número.
    cout << "Ingrese un numero: ";
    cin >> numero;

    // El ciclo while se ejecuta mientras el contador sea menor o igual a 10.
    while (contador <= 10)
    {
        // Muestra el resultado de la multiplicación.
        cout << numero << " x " << contador
            << " = " << numero * contador << endl;

        // Aumenta el contador en 1.
        contador++;
    }

    // Indica que el programa terminó correctamente.
    return 0;
}
