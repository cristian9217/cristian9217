/**
 * File: InputValidation.cpp
 * Author: Prof. Cristian M. Pagán
 * Course: COSC 131 - Programming Logic
 * Date: 29-septiembre-2026
 * Description: Demuestra el uso de múltiples bloques catch para
 * manejar diferentes tipos de excepciones durante la validación
 * de datos ingresados por el usuario.
 */
 
#include <iostream>
 
// Permite utilizar excepciones estándar.
#include <stdexcept>
 
using namespace std;
 
int main()
{
    // Declara la variable para almacenar la opción del menú.
    int opcion;
 
    // Repite el menú hasta que el usuario seleccione la opción 4.
    do
    {
        // Muestra el menú de opciones.
        cout << "===== INPUT VALIDATION MENU =====" << endl;
        cout << "1. Enter an Integer" << endl;
        cout << "2. Enter a Double" << endl;
        cout << "3. Enter a String" << endl;
        cout << "4. Exit" << endl;
        cout << endl;
 
        // Solicita al usuario que seleccione una opción.
        cout << "Enter your choice: ";
        cin >> opcion;
 
        // Verifica si la opción ingresada es válida.
        if (cin.fail())
        {
            // Limpia el estado de error de cin.
            cin.clear();
 
            // Elimina la entrada incorrecta.
            cin.ignore(1000, '\n');
 
            // Muestra un mensaje de error.
            cout << "Error: Please enter a valid menu option." << endl;
            cout << endl;
 
            // Continúa con la siguiente iteración del ciclo.
            continue;
        }
 
        // Verifica que la opción esté entre 1 y 4.
        if (opcion < 1 || opcion > 4)
        {
            cout << "Error: Invalid menu option." << endl;
            cout << endl;
            continue;
        }
 
        // Termina el programa si el usuario selecciona la opción 4.
        if (opcion == 4)
        {
            cout << "Program terminated." << endl;
            break;
        }
 
        try
        {
            switch(opcion)
            {
                case 1: 
                {
                    // Procesa la opción 1: ingresar un entero.
                    int numero;
 
                    cout << "Enter an integer: ";
                    cin >> numero;
 
                    // Verifica si la entrada no es un entero.
                    if (cin.fail())
                    {
                        cin.clear();
                        cin.ignore(1000, '\n');
 
                        // Lanza una excepción de tipo int.
                        throw 1;
                    }
 
                    cout << "Integer entered: " << numero << endl;
                    break;
                }
                case 2:
                {
                    // Procesa la opción 2: ingresar un double.
                    double numero;
 
                    cout << "Enter a double: ";
                    cin >> numero;
 
                    // Verifica si la entrada no es un número decimal válido.
                    if (cin.fail())
                    {
                        cin.clear();
                        cin.ignore(1000, '\n');
 
                        // Lanza una excepción de tipo double.
                        throw 1.0;
                    }
 
                    cout << "Double entered: " << numero << endl;
                    break;
                }
                case 3:
                {
                    // Procesa la opción 3: ingresar un string.
                    string texto;
 
                    cout << "Enter a string: ";
                    cin >> texto;
 
                    // Verifica si ocurrió un error durante la entrada.
                    if (cin.fail())
                    {
                        cin.clear();
                        cin.ignore(1000, '\n');
 
                        // Lanza una excepción de tipo string.
                        throw string("Invalid string input.");
                    }
 
                    cout << "String entered: " << texto << endl;
                }
            }            
        }
 
        catch (int error)
        {
            // Captura una excepción de tipo int.
            cout << "Error: Invalid integer input." << endl;
        }
        catch (double error)
        {
            // Captura una excepción de tipo double.
            cout << "Error: Invalid double input." << endl;
        }
        catch (string error)
        {
            // Captura una excepción de tipo string.
            cout << "Error: " << error << endl;
        }
 
        cout << endl;
 
    } while (opcion != 4);
 
    return 0;
}
