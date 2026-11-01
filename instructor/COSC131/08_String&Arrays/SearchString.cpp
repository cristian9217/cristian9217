/**
 * File: SearchString.cpp
 * Author: Prof. Cristian M. Pagán
 * Course: COSC 131 - Programming Logic
 * Date: 31-octubre-2026
 * Description: Este programa demuestra el uso
 * de diferentes funciones de la clase string en C++.
 */

#include <iostream>

using namespace std;

/**
 * Busca una palabra dentro de un string.
 * @param texto string donde se realizará la búsqueda.
 * @param clave Palabra que se desea encontrar.
 */
static void find(string texto, string clave)
{
    printf("Buscar '%s' fue encontrada ", clave.c_str());
    cout << "en la posicion : " << texto.find(clave) << endl;
}

/**
 * Busca un carácter dentro de un string desde una posición específica.
 * @param texto string donde se realizará la búsqueda.
 * @param letter Carácter que se desea encontrar.
 */
static void findFrom(string texto, string letter)
{
    printf("Buscar '%s' desde la posicion 10: ", letter.c_str());
    cout << texto.find(letter, 10) << endl;
}

/**
 * Busca la primera aparición de cualquiera de los caracteres indicados.
 * @param texto string donde se realizará la búsqueda.
 * @param caracteres Caracteres que se desean encontrar.
 */
static void findFirst(string texto, string caracteres)
{
    cout << "Posicion de la primera vocal: ";
    cout << texto.find_first_of(caracteres, 0) << endl;
}

/**
 * Busca el primer carácter que no coincida con los caracteres indicados.
 * @param texto string donde se realizará la búsqueda.
 * @param caracteres Caracteres que se desean excluir.
 */
static void findFirstNot(string texto, string caracteres)
{
    cout << "Posicion del primer caracter no vocal: ";
    cout << texto.find_first_not_of(caracteres, 0) << endl;
}

/* Función principal del programa. */
int main()
{
    // El texto que se desea buscar.
    string texto = "Tu me das la verde y yo voy";

    // Muestra la frase original.
    cout << "Frase: " << texto << endl << endl;

    // Busca la palabra "verde" dentro de la frase.
    find(texto, "verde");

    // Busca la letra "o" a partir de la posición 10.
    findFrom(texto, "o");

    // Busca la primera aparición de una vocal.
    findFirst(texto, "aeiou");

    // Busca el primer carácter que no sea una vocal.
    findFirstNot(texto, "aeiou");

    // Finaliza la ejecucion del programa.
    return 0;
}
