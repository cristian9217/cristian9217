/*
 * File: secret_number.cpp
 * Author: Cristian M. Pagan
 * Course: COSC 131 - Programming Logic
 * Date: August 10, 2026
 * Description: Este programa permite al usuario intentar adivinar 
 * un número secreto entre 1 y 100 utilizando un ciclo do-while.
 */

#include <iostream>

using namespace std;

int main() 
{
    // Se declara el número secreto.
    int numeroSecreto = 50;

    // Se declara la variable para almacenar el intento del usuario.
    int intento;

    // El ciclo se ejecuta al menos una vez y continúa hasta adivinar.
    do 
    {
        // Solicita al usuario que introduzca un número.
        cout << "Adivina el numero secreto entre 1 y 100: ";
        cin >> intento;

        // Verifica si el número secreto es mayor que el intento.
        if (intento < numeroSecreto) 
        {
            cout << "El numero secreto es mayor." << endl;
        }
        // Verifica si el número secreto es menor que el intento.
        else if (intento > numeroSecreto) 
        {
            cout << "El numero secreto es menor." << endl;
        }

    } while (intento != numeroSecreto);

    // Se muestra el mensaje cuando el usuario adivina correctamente.
    cout << "¡Felicidades! Has ganado." << endl;

    // Indica que el programa terminó correctamente.
    return 0;
}
