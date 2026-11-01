/**
 * File: ModifyString.cpp
 * Author: Prof. Cristian M. Pagán
 * Course: COSC 131 - Programming Logic
 * Date: 31-octubre-2026
 * Description: Este programa demuestra el uso 
 * de diferentes funciones de la clase string en C++.
 */
 
#include <iostream>
 
using namespace std;

/**
 * Elimina todo el contenido de un string usando clear().
 * @param texto Cadena que se desea vaciar.
 */
static void clear(string texto)
{
    texto.clear();
    cout << texto << endl;
}

/**
 * Elimina todo el contenido de un string usando erase().
 * @param texto Cadena que se desea vaciar.
 */
static void erase(string texto)
{
    texto.erase();
    cout << texto << endl;
}

/**
 * Elimina una cantidad de caracteres desde la posición 0.
 * @param texto Cadena que se desea modificar.
 * @param end Cantidad de caracteres que se eliminarán.
 */
static void erase(string texto, int end)
{
    texto.erase(0, end);
    cout << texto << endl;
}

/**
 * Reemplaza la palabra "mundo" por un texto nuevo.
 * @param nuevoTexto Texto que reemplazará la palabra original.
 */
static void replace(string nuevoTexto)
{
    string texto = "Hola mundo";
    texto.replace(5, 5, nuevoTexto);
    cout << texto << endl;
}

/**
 * Extrae una parte de una cadena usando substr().
 * @param start Posición inicial de la extracción.
 * @param end Cantidad de caracteres que se extraerán.
 */
static void substring(int start, int end)
{
    string texto = "Introduccion a la Logica de Programacion";
    string parte = texto.substr(start, end);
    cout << parte << endl;
}

/**
 * @brief Intercambia el contenido de dos cadenas usando swap().
 * @param str1 Primer string que se va a intercambiar.
 * @param str2 Segundo string que se va a intercambiar.
 */
static void swap(string str1, string str2)
{
    cout << "\nAntes del intercambio: "; 
    cout << str1 << ", " << str2 << endl;
    
    str1.swap(str2);
 
    cout << "Despues del intercambio: ";
    cout << str1 << ", " << str2 << endl;
}

/* Función principal del programa. */
int main() 
{
    // Ejecuta la función clear() con el string "Hola mundo".
    cout << "Eliminando todo el contenido con clear():" << endl;
    clear("Hola mundo");
 
    // Ejecuta erase() para borrar todo el contenido del string.
    cout << "\nEliminando todo el contenido con erase():" << endl;
    erase("Anuelcito");
 
    // Elimina los primeros 5 caracteres del string "Hola mundo".
    cout << "\nEliminando los primeros 5 caracteres: " << endl;
    erase("Hola mundo", 5);
 
    // Reemplaza la palabra 'mundo' por 'amigo' en string.
    cout << "\nReemplazando 'mundo' por 'amigo': " << endl;
    replace("amigo");
 
    // Extrae 5 caracteres comenzando desde la posición 0.
    cout << "\nExtrayendo los primeros 5 caracteres: " << endl;
    substring(0, 5);
 
    // Intercambia el contenido del string "Manzana" y "Naranja".
    swap("Manzana", "Naranja");
 
    // Finaliza el programa correctamente.
    return 0;
}
