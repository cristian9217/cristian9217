/**
 * File: sum_numbers.cpp
 * Author: Cristian M. Pagan
 * Course: COSC 131 - Programming Logic
 * Date: August 10, 2026
 * Description: Este programa solicita 5 números 
 * al usuario y calcula la suma de todos los 
 * números ingresados.
 */

#include <iostream>

using namespace std;

// Inicia la ejecución del programa.
int main() 
{
    // Se declaran las variables.
    int numero;
    int suma = 0;
    int contador = 1;

    // El ciclo while se ejecuta.
    while (contador < 6) 
    {
        // Solicita al usuario que ingrese un número.
        cout << "Ingrese el numero " << contador << ": ";
        cin >> numero;

        // Se suma el número ingresado al total acumulado.
        suma += numero;

        // Aumenta el contador en 1.
        contador++;
    }

    // Muestra el resultado final de la suma.
    cout << endl;
    cout << "La suma total es: " << suma << endl;

    // Indica que el programa terminó correctamente.
    return 0;
}
