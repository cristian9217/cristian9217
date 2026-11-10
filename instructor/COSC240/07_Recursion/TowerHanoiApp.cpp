/**
 * File: TowerHanoiApp.cpp
 * Author: Prof. Cristian M. Pagan
 * Course: COSC 240 - Computer Science Programming II
 * Date: 6-noviembre-2026
 * Description: Demuestra el uso de funciones recursivas para 
 * resolver el problema matemático de las Torres de Hanoi.
 */

#include "TowerOfHanoi.h"
#include <iostream>

using namespace std;

// Función principal del programa.
int main() 
{
    int numDiscs;

    // Solicita al usuario la cantidad de discos.
    cout << "Enter the number of discs: ";
    cin >> numDiscs;
    cout << endl;

    // Valida que la cantidad de discos sea positiva.
    if (numDiscs < 1) 
    {
        cerr << "Fatal error: Cannot move less than 1 disc." << endl;
        return 1; 
    }

    // Crea un objeto de la clase TowerOfHanoi.
    TowerOfHanoi game(numDiscs);

    // Ejecuta el algoritmo para resolver las Torres de Hanoi.
    game.solve();

    // Muestra los pasos necesarios para resolver el problema.
    cout << "Steps to solve with " << numDiscs;
    cout << " discs:\n" << game.getSteps();
    cout << endl;

    // Muestra la cantidad total de movimientos realizados.
    cout << "The number of movements was "; 
    cout << game.getMovements() << endl;
    cout << endl;

    // Indica que la aplicación ha finalizado.
    cout << "End of application." << endl;

    // Finaliza correctamente la ejecución del programa.
    return 0; 
}