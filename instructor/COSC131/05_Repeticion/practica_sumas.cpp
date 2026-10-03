/*
 * File: practica_sumas.cpp
 * Author: Prof. Cristian M. Pagan
 * Course: COSC 131 - Programming Logic
 * Date: 5-octubre-2026
 * Description: Permite al estudiante practicar sumas sencillas
 *              y verificar sus respuestas.
 */

#include <iostream>

// Incluye la biblioteca para generar números aleatorios.
#include <cstdlib>

using namespace std;

// Inicia la ejecución del programa.
int main()
{
    int numero, numero2;
    int respuesta;
    int resultado;
    char continuar = 's';

    do
    {
        // Genera dos números entre 1 y 10.
        numero = rand() % 10 + 1;
        numero2 = rand() % 10 + 1;

        // Calcula el resultado correcto.
        resultado = numero + numero2;

        // Presenta la operación al estudiante.
        cout << "Cuanto es " << numero
            << " + " << numero2 << "? ";
        cin >> respuesta;

        cout << endl;

        // Verifica si la respuesta es correcta.
        if (respuesta == resultado)
        {
            cout << "Correcto!" << endl;
        }
        else
        {
            cout << "Incorrecto." << endl;
            cout << "La respuesta correcta es "
                << resultado << "." << endl;
        }

        // Pregunta si el estudiante desea continuar.
        cout << "Desea continuar practicando? (s/n): ";
        cin >> continuar;

        cout << endl;

    } while (continuar == 's' || continuar == 'S');

    // Muestra un mensaje al finalizar la práctica.
    cout << "Fin de la practica." << endl;

    return 0;
}
