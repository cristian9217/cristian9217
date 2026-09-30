/**
 * File: EmployeeApp.cpp
 * Author: Prof. Cristian M. Pagán
 * Course: COSC 131 - Programming Logic
 * Date: 29-septiembre-2026
 * Description: Crea objetos de la clase Employee, muestra información
 * válida y demuestra el manejo de excepciones para datos inválidos.
 */

#include <iostream>
#include <iomanip>

// Incluye la clase Employee.
#include "Employee.h"

using namespace std;

int main()
{
    // Prueba la creación de un empleado con información válida.
    try
    {
        // Crea un empleado con datos válidos.
        Employee employee("12345", 30, 45000.00);

        // Muestra la información del empleado.
        cout << "===== VALID EMPLOYEE =====" << endl;
        cout << "Employee ID: " << employee.getEmployeeId() << endl;
        cout << "Age: " << employee.getAge() << endl;
        cout << fixed << setprecision(2);
        cout << "Salary: $" << employee.getSalary() << endl;
    }
    catch (const invalid_argument& error)
    {
        // Muestra el error si los datos del empleado no son válidos.
        cout << "Error: " << error.what() << endl;
    }

    cout << endl;

    // Prueba una edad inválida.
    try
    {
        // Intenta crear un empleado con una edad menor de 16.
        Employee employee("12345", 15, 45000.00);
    }
    catch (const invalid_argument& error)
    {
        // Muestra el error relacionado con la edad.
        cout << "Age Error: " << error.what() << endl;
    }

    // Prueba un salario inválido.
    try
    {
        // Intenta crear un empleado con un salario negativo.
        Employee employee("12345", 30, -5000.00);
    }
    catch (const invalid_argument& error)
    {
        // Muestra el error relacionado con el salario.
        cout << "Salary Error: " << error.what() << endl;
    }

    // Prueba un ID inválido.
    try
    {
        // Intenta crear un empleado con un ID que contiene letras.
        Employee employee("12A45", 30, 45000.00);
    }
    catch (const invalid_argument& error)
    {
        // Muestra el error relacionado con el ID.
        cout << "ID Error: " << error.what() << endl;
    }

    return 0;
}
