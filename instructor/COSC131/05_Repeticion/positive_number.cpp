/*
* File: positive_number.cpp
* Author: Cristian M. Pagan
* Course: COSC 131 - Programming Logic
* Date: August 10, 2026
* Description: Este programa solicita números al usuario hasta que
*              se introduzca un número positivo utilizando un ciclo while.
*/

#include <iostream>

using namespace std;

// Inicia la ejecución del programa.
int main()
{
    // Se declara la variable para almacenar el número.
    int numero;

    // Solicita al usuario que ingrese un número.
    cout << "Ingrese un numero: ";
    cin >> numero;

    // El ciclo while continúa mientras el número no sea positivo.
    while (numero <= 0)
    {
        // Informa al usuario que debe ingresar un número positivo.
        cout << "El numero debe ser positivo." << endl;

        // Solicita nuevamente un número.
        cout << "Ingrese un numero: ";
        cin >> numero;
    }

    // Muestra el número positivo ingresado.
    cout << "Numero positivo: " << numero << endl;

    // Indica que el programa terminó correctamente.
    return 0;
}
