/*
* File: countdown.cpp
* Author: Cristian M. Pagan
* Course: COSC 131 - Programming Logic
* Date: August 10, 2026
* Description: Este programa demuestra el uso de 
* un ciclo while para realizar una cuenta regresiva 
* de 10 a 1.
*/

#include <iostream>

using namespace std;

// Inicia la ejecución del programa.
int main() 
{
    // Se declara la variable contador y se inicializa en 10
    int contador = 10;

    // El ciclo while se ejecuta mientras contador sea mayor que 0
    while (contador > 0) 
    {
        // Muestra el valor actual del contador
        cout << contador << endl;

        // Disminuye el contador en 1
        contador--;
    }

    // Cuando el contador llega a 0. 
    cout << "Despegue..." << endl;

    // Indica que el programa terminó correctamente.
    return 0;
}
