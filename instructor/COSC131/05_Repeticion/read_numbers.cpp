/*
* File: read_numbers.cpp
* Author: Cristian M. Pagan
* Course: COSC 131 - Programming Logic
* Date: August 10, 2026
* Description: Este programa lee números de un archivo 
* y calcula el total utilizando un ciclo while.
*/

#include <iostream>
#include <fstream>

using namespace std;

// Inicia la ejecución del programa.
int main()
{
    // Declara la variable para almacenar cada número.
    int numero;

    // Declara la variable para almacenar el total.
    int total = 0;

    // Declara el archivo de entrada.
    ifstream inputFile;

    // Abre el archivo.
    inputFile.open("numbers.txt");

    // Verifica si el archivo pudo abrirse correctamente.
    if (inputFile.is_open())
    {
        // Lee los números mientras haya datos en el archivo.
        while (inputFile >> numero)
        {
            // Suma cada número al total.
            total += numero;
        }
        
        // Cierra el archivo.
        inputFile.close();
    }
    else
    {
        cout << "No se pudo abrir el archivo." << endl;
        return 1;
    }

    // Muestra el total de los números.
    cout << "El total es: " << total << endl;

    // Indica que el programa terminó correctamente.
    return 0;
}
