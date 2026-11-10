/**
 * File: RecursiveInteger.cpp
 * Author: Prof. Cristian M. Pagan
 * Course: COSC 240 - Computer Science Programming II
 * Date: 6-noviembre-2026
 * Description: Demuestra el uso de funciones recursivas
 * para calcular el factorial de un número entero no negativo.
 */

#include <stdexcept>

using namespace std;

/* Clase que contiene metodos recursivos. */
class RecursiveInteger
{
    private:
        /**
         * Calcula un número de la secuencia de Fibonacci mediante recursión.
         * @param num Posición del número que se desea calcular.
         */
        static long fibonacciHelper(int num) {
            if (num == 0 || num == 1)
                return num;

            return fibonacciHelper(num - 1) + fibonacciHelper(num - 2);
        }


        /**
         * Calcula el factorial del número utilizando recursión
         * @param num El número entero que se desea verificar.
         */
        static long factorialHelper(long int num)
        {
            // Caso base
            if (num == 0)
                return 1;

            // Caso general
            return num * factorialHelper(num - 1);
        }

        /**
         * Verifica que el número entero especificado no sea negativo.
         * @param num El número entero que se desea verificar.
         * @throws invalid_argument si el número es negativo.
         */
        static void checkNotNegative(int num) {
            if (num < 0)
                throw invalid_argument("Invalid negative integer!");
        }

    public:
        /*
         * Calcula el número de Fibonacci correspondiente a una posición.
         * @param num Posición del número que se desea calcular.
         * @return El valor de Fibonacci correspondiente a la posición.
         */
        static long fibonacci(int num)
        {
            checkNotNegative(num);
            return fibonacciHelper(num);
        }
        
        /**
         * Devuelve el factorial del número entero no negativo.
         * @param num El número cuyo factorial se desea calcular.
         * @return El factorial del número.
         */
        static long factorial(long int num)
        {
            checkNotNegative(num);
            return factorialHelper(num);
        }
};