/*
 * File: funciones.cpp
 * Author: Prof. Cristian M. Pagan
 * Course: COSC 131 - Programming Logic
 * Date: 5-octubre-2026
 * Description: Demuestra el uso de funciones void y 
 * funciones que retornan un valor en C++.
 */

#include <iostream>
#include <string>

using namespace std;

/*
 * Muestra un saludo utilizando el nombre. 
 * @param nombre Nombre de la persona que recibira el saludo.
 */
static void saludar(string nombre)
{
    cout << "Saludos, " << nombre << endl;
}

/*
 * Calcula el cuadrado de un numero entero. 
 * @param numero Numero que se desea elevar al cuadrado.
 * @return El cuadrado del numero recibido.
 */
static int cuadrado(int numero)
{
    return numero * numero;
}


// Inicia la ejecución del programa.
int main()
{
    // Muestra un mensaje antes de comenzar los saludos.
    cout << "Saludando a los colega..." << endl;
    
    // Llama a la función saludar para cada colega.
    saludar("Jose");
    saludar("Mario");
    saludar("Kevin");

    cout << endl;

    // Llama a la función cuadrado y guarda el valor retornado.
    int resultado = cuadrado(5);

    // Muestra el resultado del cálculo.
    cout << "El cuadrado es: " << resultado << endl;

    return 0;
}
