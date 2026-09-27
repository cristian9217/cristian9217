/*
* File: negative_numbers.cpp
* Author: Cristian M. Pagan
* Course: COSC 131 - Programming Logic
* Date: September 27, 2026
* Description: Este programa solicita 10 números 
* enteros y utiliza un ciclo for para determinar 
* cuántos son negativos.
*/

#include <iostream>

using namespace std;

// Inicia la ejecución del programa.
int main()
{
    // Declara las variables.
    int number;
    int negativeCount = 0;

    // Repite el proceso 10 veces.
    for (int counter = 1; counter < 11; counter++)
    {
        // Solicita un número al usuario.
        cout << "Ingrese el numero " << counter << ": ";
        cin >> number;

        // Verifica si el número es negativo.
        if (number < 0)
        {
            negativeCount++;
        }
    }

    // Muestra la cantidad de números negativos.
    cout << "Cantidad de numeros negativos: ";
    cout << negativeCount << endl;

    // Indica que el programa terminó correctamente.
    return 0;
}
