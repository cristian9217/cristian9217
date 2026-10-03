/**
 * File: analizar_datos.cpp
 * Author: Prof. Cristian M. Pagán
 * Course: COSC 131 - Programming Logic
 * Date: 12-septiembre-2026
 * Description: Lee una serie de números desde un archivo de
 * entrada y genera un resumen en un archivo de salida.
 */

// Incluye la biblioteca que permite utilizar cout y endl.
#include <iostream>

// Incluye la biblioteca necesaria para trabajar con archivos. 
#include <fstream>

using namespace std;

// Inicia la ejecución del programa.
int main()
{
    // Declara el archivo de entrada.
    ifstream inputFile;

    // Declara el archivo de salida.
    ofstream outputFile;

    // Abre el archivo de entrada.
    inputFile.open("datos.txt");

    // Verifica si el archivo de entrada pudo abrirse.
    if (!inputFile.is_open())
    {
        cout << "No se pudo abrir el archivo de entrada." << endl;
        return 1;
    }

    // Abre el archivo de salida.
    outputFile.open("resultados.txt");

    // Verifica si el archivo de salida pudo abrirse.
    if (!outputFile.is_open())
    {
        cout << "No se pudo abrir el archivo de salida." << endl;
        return 1;
    }

    // Variables para procesar los datos.
    int number, count = 0;
    int smallest, largest;
    double sum = 0.0;

    if (inputFile)
    {
        // Lee el primer número del archivo.
        inputFile >> number;

        // Inicializa el menor y el mayor.
        smallest = number;
        largest = number;

        // Procesa los números del archivo.
        while (!inputFile.eof())
        {
            // Cuenta el número procesado.
            count++;

            // Acumula la suma.
            sum = sum + number;

            // Determina el número menor.
            if (number < smallest)
                smallest = number;

            // Determina el número mayor.
            if (number > largest)
                largest = number;

            // Lee el siguiente número.
            inputFile >> number;
        }

        // Calcula el promedio.
        double average = sum / count;

        // Escribe los resultados en el archivo de salida.
        outputFile << "Cantidad de numeros: " << count << endl;
        outputFile << "Numero menor: " << smallest << endl;
        outputFile << "Numero mayor: " << largest << endl;
        outputFile << "Suma: " << sum << endl;
        outputFile << "Promedio: " << average << endl;
    }

    // Cierra el archivo de entrada.
    inputFile.close();

    // Cierra el archivo de salida.
    outputFile.close();

    return 0;
}
