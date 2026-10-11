/**
 * File: FileOpeningException.cpp
 * Author: Prof. Cristian M. Pagán
 * Course: COSC 131 - Programming Logic
 * Date: 29-septiembre-2026
 * Description: Solicita el nombre de un archivo de texto, intenta
 * abrirlo utilizando ifstream y utiliza excepciones para manejar
 * errores cuando el archivo no puede ser abierto.
 */

#include <iostream>
#include <string>

// Permite trabajar con archivos de entrada.
#include <fstream>

using namespace std;

int main()
{
    // Declara la variable para almacenar el nombre del archivo.
    string nombreArchivo;

    // Controla si el archivo fue abierto correctamente.
    bool archivoAbierto = false;
    do
    {
        try
        {
            // Solicita al usuario el nombre del archivo.
            cout << "Enter the name of the text file: ";
            cin >> nombreArchivo;

            // Crea un objeto ifstream para leer el archivo.
            ifstream inputFile;

            // Intenta abrir el archivo especificado por el usuario.
            inputFile.open(nombreArchivo);

            // Verifica si el archivo no pudo ser abierto.
            if (!inputFile.is_open())
            {
                // Genera una excepción si el archivo no puede abrirse.
                throw runtime_error("The file could not be opened.");
            }

            if (inputFile)
            {
                // Informa que el archivo fue abierto correctamente.
                cout << "File opened successfully." << endl;
                cout << endl;

                // Declara una variable para almacenar cada línea del archivo.
                string linea;

                // Lee y muestra el archivo línea por línea.
                cout << "File contents: " << endl;
                while (getline(inputFile, linea))
                {
                    cout << linea << endl;
                }
            }

            // Cierra el archivo después de leer su contenido.
            inputFile.close();

            // Indica que el archivo fue abierto correctamente.
            archivoAbierto = true;
        }
        catch (const runtime_error err)
        {
            // Muestra el mensaje de error cuando el archivo no puede abrirse.
            cout << "Error: " << err.what() << endl;
        }
    } while (!archivoAbierto);

    return 0;
}
