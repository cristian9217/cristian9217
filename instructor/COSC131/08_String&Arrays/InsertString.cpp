/**
 * File: InsertString.cpp
 * Author: Prof. Cristian M. Pagán
 * Course: COSC 131 - Programming Logic
 * Date: 31-octubre-2026
 * Description: Este programa demuestra el uso 
 * de diferentes funciones de la clase string en C++.
 */
 
#include <iostream>
 
using namespace std;
 
/* 
 * Inserta caracteres en el string
 * @param texto String que será modificada.
 * @param element Carácter que se desea insertar.
 */
static void insert(string texto, char element)
{
    texto.insert(16, 3, element);
    cout << texto << endl;
}
 
/* 
 * Inserta una frase en el string
 * @param texto String que será modificada.
 * @param word Frase que se desea insertar.
 */
static void insert(string texto, string word)
{
    texto.insert(16, word);
    cout << texto << endl;
}
 
/* Función principal del programa. */
int main() 
{
    string texto = "Tengo una virtud";
 
    // Muestra el string original.
    cout << "Imprime la frase: " << texto;
    cout << endl << endl;
    
    // Inserta punto al final de la cadena.
    insert(texto, '.');
 
    // Inserta una frase en la posición especificada.
    insert(texto, " A mi me cuida San Miguel");
    cout << endl;
    
    string texto2 = "Me gusta comer pizza";
 
    // Muestra el segundo string original.
    cout << "Imprime la frase: " << texto2;
    cout << endl << endl;
 
    // Agrega tres puntos al final de la cadena.
    texto2.append(3, '.');
    cout << texto2 << endl;
 
    // Agrega una frase al final de la cadena.
    texto2.append(" con pepperoni.");
    cout << texto2 << endl;
 
    // Finaliza el programa correctamente.
    return 0;
}
