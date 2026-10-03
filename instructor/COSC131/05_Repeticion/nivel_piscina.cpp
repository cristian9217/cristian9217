/*
 * File: nivel_piscina.cpp
 * Author: Prof. Cristian M. Pagan
 * Course: COSC 131 - Programming Logic
 * Date: 5-octubre-2026
 * Description: Simula el aumento del nivel de agua de 
 * una piscina hasta alcanzar el nivel máximo de 
 * 100 centímetros.
 */

#include <iostream>

using namespace std;

// Inicia la ejecución del programa. 
int main()
{
    // Establece el nivel inicial de la piscina en 10 centímetros.
    int nivel = 10;

    // Continúa aumentando el nivel hasta llegar a 100 centímetros.
    do 
    {
        // Aumenta el nivel de agua en 10 centímetros.
        nivel = nivel + 10;

        // Muestra el nivel actual de la piscina.
        cout << "Nivel de agua: " << nivel;
        cout << " cm" << endl;

    } while (nivel < 100);

    // Indica que la piscina alcanzó su nivel máximo.
    cout << "La piscina alcanzo el nivel maximo." << endl;

    return 0;
}
