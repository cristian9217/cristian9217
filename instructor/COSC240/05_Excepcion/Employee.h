/**
 * File: Employee.h
 * Author: Prof. Cristian M. Pagán
 * Course: COSC 131 - Programming Logic
 * Date: 29-septiembre-2026
 * Description: Declara la clase Employee, sus atributos, constructor
 * y métodos para validar la información de un empleado.
 */

#include <string>
#include <stdexcept>

using namespace std;

/** Esta clase representa a un Empleado. */
class Employee
{
    private:
        /* El ID del empleado. */
        string employeeId;

        /* La edad del empleado. */
        int age;

        /* El salario del empleado. */
        double salary;

    public:
        /**
         * Constructor de la clase Employee.
         * @param employeeId Identificador de cinco dígitos.
         * @param age Edad del empleado.
         * @param salary Salario del empleado.
         */
        Employee(string employeeId, int age, double salary)
        {
            setEmployeeId(employeeId);
            setAge(age);
            setSalary(salary);
        }

        /**
         * Valida y establece el identificador del empleado.
         * @param employeeId Identificador del empleado.
         * @throws invalid_argument Si el ID no contiene exactamente
         * cinco caracteres numéricos.
         */
        void setEmployeeId(string employeeId)
        {
            // Verifica que el ID tenga exactamente cinco caracteres.
            if (employeeId.length() != 5)
                throw invalid_argument("Invalid employee ID.");
            this->employeeId = employeeId;
        }

        /**
         * Valida y establece la edad del empleado.
         * @param age Edad del empleado.
         * @throws invalid_argument Si la edad es menor de 16 o mayor de 120.
         */
        void setAge(int age)
        {
            if (age < 16 || age > 120)
                throw invalid_argument("Invalid employee age.");
            this->age = age;
        }

        /**
         * Valida y establece el salario del empleado.
         * @param salary Salario del empleado.
         * @throws invalid_argument Si el salario es negativo.
         */
        void setSalary(double salary)
        {
            if (salary < 0)
                throw invalid_argument("Invalid employee salary.");
            this->salary = salary;
        }

        /**
         * Devuelve el identificador del empleado.
         * @return El ID del empleado.
         */
        string getEmployeeId()
        {
            return employeeId;
        }

        /**
         * Devuelve la edad del empleado.
         * @return La edad del empleado.
         */
        int getAge()
        {
            return age;
        }

        /**
         * Devuelve el salario del empleado.
         * @return El salario del empleado.
         */
        double getSalary()
        {
            return salary;
        }
};
