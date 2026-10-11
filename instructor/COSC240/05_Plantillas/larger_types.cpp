/**
 * File: larger_types.cpp
 * Author: Prof. Cristian M. Pagán
 * Course: COSC 240 - Computer Science Programming II
 * Date: 11-octubre-2026
 * Description: Programa para demostrar el uso de function 
 * templates en C++. Utiliza la función larger para comparar
 * dos valores y devolver el mayor.
 */

#include <iostream>
 
using namespace std;

/**
 * Devuelve el mayor de dos valores.
 * @tparam Type Tipo de dato de los valores.
 * @param a Primer valor que se compara.
 * @param b Segundo valor que se compara.
 * @return El mayor de los dos valores.
 */
template <typename Type>
Type larger(Type a, Type b) 
{
    return (a > b) ? a : b;
}

/**
 * Devuelve el menor de dos valores.
 * @tparam Type Tipo de dato de los valores.
 * @param a Primer valor que se compara.
 * @param b Segundo valor que se compara.
 * @return El menor de los dos valores.
 */
template <typename Type>
Type smaller(Type a, Type b)
{
    return (a < b) ? a : b;
}

// Inicia la ejecución del programa.
int main()
{
    // Compara dos enteros y muestra el mayor.
    cout << "Mayor: " << larger(10, 20) << endl;

    // Compara dos decimales y muestra el mayor.
    cout << "Mayor: " << larger(3.5, 2.1) << endl;
    cout << endl;

    // Compara dos enteros y muestra el menor.
    cout << "Menor: " << smaller(10, 20) << endl;

    // Compara dos decimales y muestra el menor.
    cout << "Menor: " << smaller(3.5, 2.1) << endl;

    // Finaliza el programa.
    return 0;
}
