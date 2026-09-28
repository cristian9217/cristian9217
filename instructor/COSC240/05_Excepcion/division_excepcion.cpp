/* 
 * File: division_excepcion.cpp 
 * Author: Cristian M. Pagan 
 * Course: COSC 240 - Computer Science Programming II 
 * Date: September 27, 2026 
 * Description: Este programa solicita dos números decimales 
 * al usuario y realiza una división. Utiliza manejo de 
 * excepciones para evitar la división entre cero. 
 */

// Permite utilizar cout y cin. 
#include <iostream>

// Permite establecer el formato de los números. 
#include <iomanip>

// Permite utilizar invalid_argument.
#include <stdexcept> 

using namespace std;

int main() 
{
    try 
    {
        // Variables que almacenarán el dividendo y el divisor.
        double dividendo, divisor;

        // Solicita al usuario el número que será dividido.
        cout << "Ingrese el dividendo: ";
        cin >> dividendo;

        // Solicita al usuario el número por el cual se dividirá.
        cout << "Ingrese el divisor: ";
        cin >> divisor;

        // Verifica si el divisor es cero y lanza una expecion.
        if (divisor == 0)
            throw invalid_argument("No se puede dividir entre cero.");

        // Realiza la división si el divisor es diferente de cero.
        double resultado = dividendo / divisor;

        // Configura la salida para mostrar dos posiciones decimales.
        cout << fixed << setprecision(2);

        // Muestra la operación y el resultado.
        cout << dividendo << " / " << divisor << " = ";
        cout << resultado << endl;

    }
    catch (invalid_argument msg) 
    {
        // Muestra el mensaje de error utilizando what().
        cout << "Error: " << msg.what() << endl;
    }

    // Indica que el programa terminó correctamente.
    return 0;
}
