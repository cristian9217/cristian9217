/**
 * File: AgeValidationApp.cpp
 * Author: Prof. Cristian M. Pagán
 * Course: COSC 131 - Programming Logic
 * Date: 29-septiembre-2026
 * Description: Solicita la edad del usuario, valida que esté entre
 * 0 y 120 años y determina la categoría correspondiente.
 */
 
#include <iostream>
 
// Permite utilizar excepciones estándar.
#include <stdexcept>
 
using namespace std;
 
/**
 * Solicita y valida la edad ingresada por el usuario.
 * @return La edad válida ingresada por el usuario.
 * @throws invalid_argument Si la edad está fuera del rango de 0 a 120.
 */
static int readAge()
{
    // Declara la variable para almacenar la edad.
    int age;
 
    // Solicita la edad al usuario.
    cout << "Enter your age: ";
    cin >> age;
 
    // Verifica si la entrada no es un número entero.
    if (cin.fail())
    {
        // Limpia el estado de error.
        cin.clear();
 
        // Elimina la entrada incorrecta.
        cin.ignore(1000, '\n');
 
        // Genera una excepción porque la entrada no es un entero.
        throw invalid_argument("Invalid age.");
    }
 
    // Verifica si el usuario desea terminar.
    if (age == -1)
        return age;
 
    // Verifica si la edad está fuera del rango permitido.
    if (age < 0 || age > 120)
        throw invalid_argument("Invalid age.");
 
    // Devuelve la edad si es válida.
    return age;
}
 
/**
 * Determina la categoría correspondiente a la edad.
 * @param age Edad de la persona.
 * @return La categoría correspondiente: Child, Teenager,
 * Adult o Senior.
 */
static string getCategory(int age)
{
    if (age > 0 && age <= 12)
        return "Child";
    else if (age > 13 && age <= 17)
        return "Teenager";
    else if (age > 18 && age <= 64)
        return "Adult";
    else
        return "Senior";
}
 
/**
 * Muestra la edad y la categoría correspondiente.
 * @param age Edad de la persona.
 * @param category Categoría correspondiente a la edad.
 */
static void showResults(int age, string category)
{
    // Muestra los resultados.
    cout << "Age: " << age << endl;
    cout << "Category: " << category << endl;
}
 
// Inicia la ejecución del programa.
int main()
{
    // Declara la variable para almacenar la edad.
    int age;
 
    // Repite el proceso hasta que se ingrese una edad válida.
    do
    {
        try
        {
            // Obtiene una edad válida del usuario.
            age = readAge();
 
            // Verifica si el usuario desea terminar.
            if (age == -1)
            {
                cout << "Program terminated." << endl;
            }
            else
            {
                // Determina la categoría correspondiente.
                string category = getCategory(age);
 
                // Muestra los resultados.
                showResults(age, category);
            }
 
            cout << endl;
        }
        catch (const invalid_argument& e)
        {
            // Muestra el mensaje de error.
            cout << "Error: " << e.what() << endl;
            cout << endl;
        }
    } while (age != -1);
 
    return 0;
}
