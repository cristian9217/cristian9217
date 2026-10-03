/*
 * File: math.cpp
 * Author: Prof. Cristian M. Pagan 
 * Course: COSC 131 - Programming Logic
 * Date: 5-octubre-2026
 * Description: Demuestra el uso de las funciones
 * matemáticas utilizando la biblioteca cmath.
 */

#include <iostream>

 // Incluye la biblioteca para utilizar funciones matemáticas.
#include <cmath>

using namespace std;

// Inicia la ejecución del programa.
int main()
{
    // Calcula el valor absoluto de un número entero.
    cout << "abs(-5) = " << abs(-5) << endl;

    // Redondea el número hacia el entero superior.
    cout << "ceil(4.2) = " << ceil(4.2) << endl;

    // Calcula el coseno de un ángulo expresado en radianes.
    cout << "cos(0) = " << cos(0) << endl;

    // Calcula el valor de e elevado a la potencia indicada.
    cout << "exp(1) = " << exp(1) << endl;

    // Calcula el valor absoluto de un número decimal.
    cout << "fabs(-3.5) = " << fabs(-3.5) << endl;

    // Redondea el número hacia el entero inferior.
    cout << "floor(4.8) = " << floor(4.8) << endl;

    // Eleva la base 2 a la potencia 3.
    cout << "pow(2, 3) = " << pow(2, 3) << endl;

    // Calcula la raíz cuadrada de un número.
    cout << "sqrt(25) = " << sqrt(25) << endl;

    return 0;
}
