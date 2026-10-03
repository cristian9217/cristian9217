/*
 * File: funciones_caracteres.cpp
 * Author: Prof. Cristian M. Pagan
 * Course: COSC 131 - Programming Logic
 * Date: 5-octubre-2026
 * Description: Demuestra el uso de las 
 * funciones caracteres en C++.
 */

#include <iostream>

// Incluye la biblioteca para manejar caracteres.
#include <cctype>

using namespace std;

// Inicia la ejecución del programa.
int main()
{
    // Declara una variable de tipo carácter.
    char letra;

    // Solicita una letra al usuario.
    cout << "Entre una letra: ";
    cin >> letra; 

    // Verifica si el carácter es una letra minúscula.
    if (islower(letra))
    {
        // Indica que la letra ingresada es minúscula.
        cout << "La letra es minuscula." << endl;
        
        // Convierte la letra minúscula a mayúscula.
        char mayuscula = toupper(letra);
        cout << "En mayuscula: " << mayuscula << endl;
    }
    // Verifica si el carácter es una letra mayúscula.
    else if (isupper(letra))
    {
        // Indica que la letra ingresada es mayúscula.
        cout << "La letra es mayuscula." << endl;
        
        // Convierte la letra mayúscula a minúscula.
        char minuscula = tolower(letra);
        cout << "En minuscula: " << minuscula << endl;
    }
    else
    {
        // Indica que el carácter ingresado no es una letra.
        cout << "No es una letra." << endl;
    }

    return 0;
}
