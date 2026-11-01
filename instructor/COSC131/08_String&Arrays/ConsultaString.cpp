/**
 * File: ConsultaString.cpp
 * Author: Prof. Cristian M. Pagán
 * Course: COSC 131 - Programming Logic
 * Date: 31-octubre-2026
 * Description: Este programa demuestra el uso 
 * de diferentes funciones de la clase string en C++.
 */

#include <iostream>

using namespace std;

/**
 * Comprueba si una posición es válida dentro de una cadena.
 * @param nombre string que se desea evaluar.
 * @param index Posición que se desea validar.
 * @return true si la posición es válida, 
 * false si está fuera de rango.
 */
static bool isValidPosition(string nombre, int index)
{
    return index >= 0 && index < nombre.size();
}

/**
 * Obtiene un carácter de la cadena utilizando el método at().
 * @param nombre string del que se obtiene el carácter.
 * @param index Posición del carácter que se desea obtener.
 */
static void characterAt(string nombre, int index)
{
    if (isValidPosition(nombre, index))
        cout << "Invalid position: " << index << endl;
    else
        cout << nombre.at(index);
}

/**
 * Obtiene un carácter de la cadena utilizando el operador [].
 * @param nombre string del que se obtiene el carácter.
 * @param index Posición del carácter que se desea obtener.
 */
static void getCharacter(string nombre, int index)
{
    if (isValidPosition(nombre, index))
        cout << "Invalid position: " << index << endl;
    else
        cout << nombre[index];
}

/**
 * Obtiene e imprime la longitud de una cadena utilizando length().
 * @param nombre string cuya longitud se desea conocer.
 */
static void getLength(string nombre)
{
    int length = nombre.length();
    cout << "Length de la palabra: " << length << endl;
}

/**
 * Obtiene e imprime la cantidad de caracteres utilizando size().
 * @param nombre string que se desea evaluar.
 */
static void getSize(string nombre)
{
    int size = nombre.size();
    cout << "Cantidad de caracteres: " << size << endl;
}

/**
 * Comprueba si una cadena está vacía utilizando empty().
 * @param nombre string que se desea evaluar.
 */
static void isEmpty(string nombre)
{
    if (nombre.empty())
        cout << "La cadena esta vacia";
    else
        cout << "La cadena contiene texto";
}

/**
 * Compara dos cadenas utilizando el método compare().
 * Imprime si ambas cadenas son iguales, o si la 
 * primera es menor o mayor que la segunda.
 * @param nombre Primera cadena que se desea comparar.
 * @param nombre2 Segunda cadena que se desea comparar.
 */
static void compareString(string nombre, string nombre2)
{
    if (nombre.compare(nombre2) == 0)
        cout << "Las cadenas son iguales" << endl;
    else if (nombre.compare(nombre2) < 0)
        cout << nombre << " es menor que " << nombre2 << endl;
    else
        cout << nombre << " es mayor que " << nombre2 << endl;
}

/* Función principal del programa. */
int main()
{
    // Guarda el primer nombre que usaremos.
    string nombre = "Anuelcito";

    // Acceso a un caracter utilizando la funcion at().
    cout << "Caracter en la posicion 5 (at): ";
    characterAt(nombre, 5);

    // Acceso a un caracter utilizando el operador [].
    cout << "Caracter en la posicion 5 ([]): ";
    getCharacter(nombre, 5);

    // Obtiene la longitud total de la cadena.
    getLength(nombre);

    // Obtiene la cantidad de caracteres del string.
    getSize(nombre);

    // Comprueba si el string está vacía utilizando empty().
    isEmpty(nombre);

    // Guarda el segundo nombre que se utilizará.
    string nombre2 = "Jay Wheeler";

    // Compara ambas string utilizando compare().
    compareString(nombre, nombre2);

    // Finaliza la ejecucion del programa.
    return 0;
}
