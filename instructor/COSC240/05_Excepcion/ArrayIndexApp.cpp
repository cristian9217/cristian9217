/**
 * File: ArrayIndexApp.cpp
 * Author: Prof. Cristian M. Pagán
 * Course: COSC 131 - Programming Logic
 * Date: 29-septiembre-2026
 * Description: Solicita al usuario un índice y muestra el elemento
 * correspondiente de un arreglo. Si el índice está fuera del rango
 * válido, se genera y maneja una excepción.
 */
 
#include <iostream>

// Permite utilizar excepciones estándar.
#include <stdexcept>
 
using namespace std;
 
/**
 * Verifica si el índice es válido y devuelve el elemento
 * correspondiente del arreglo.
 * @param numeros Arreglo de números enteros.
 * @param size Cantidad de elementos del arreglo.
 * @param indice Índice del elemento que se desea obtener.
 * @return El elemento almacenado en el índice indicado.
 * @throws out_of_range Si el índice está fuera del rango válido.
 */
static int obtenerElemento(int numeros[], int size, int indice)
{
    if (indice < 0 || indice >= size)
        throw out_of_range("Index out of range");
    return numeros[indice];
}
 
// Inicia la ejecución del programa.
int main()
{
    // Declara e inicializa el arreglo de números.
    int numeros[10] = { 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 };
 
    // Calcula la cantidad de elementos del arreglo.
    int size = sizeof(numeros) / sizeof(numeros[0]);
 
    // Declara la variable para almacenar el índice ingresado.
    int indice;
 
    // Repite el proceso hasta que el usuario ingrese -1.
    do
    {
        try
        {
            // Solicita al usuario un índice.
            cout << "Enter an index: ";
            cin >> indice;
 
            // Verifica si la entrada no es un número entero.
            if (cin.fail())
            {
                // Limpia el estado de error.
                cin.clear();
 
                // Elimina la entrada incorrecta.
                cin.ignore(1000, '\n');
 
                // Genera una excepción porque la entrada no es un entero.
                throw invalid_argument("Please enter an integer.");
            }
 
            // Verifica si el usuario desea terminar.
            if (indice == -1)
            {
                cout << "Program terminated." << endl;
            }
            else
            {
                // Obtiene y muestra el elemento correspondiente al índice.
                int elemento = obtenerElemento(numeros, size, indice);
                cout << "Element: " << elemento << endl;
            }
        }
        catch (const out_of_range e)
        {
            // Maneja los índices fuera del rango.
            cout << "Error: " << e.what() << endl;
        }
        catch (const invalid_argument e)
        {
            // Maneja las entradas que no son números enteros.
            cout << "Error: " << e.what() << endl;
        }
 
        cout << endl;
    } while (indice != -1);
 
    return 0;
}
