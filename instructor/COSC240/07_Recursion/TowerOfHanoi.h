/**
 * File: TowerHanoi.h
 * Author: Prof. Cristian M. Pagan
 * Course: COSC 240 - Computer Science Programming II
 * Date: 6-noviembre-2026
 * Description: Define la clase TowerOfHanoi para
 * resolver el problema de las Torres de Hanoi.
 */

#include <string>

using namespace std;

/* Esta clase resuelve el juego de las Torres de Hanoi. */
class TowerOfHanoi 
{
    private:
        /** Número de discos que se deben mover. */
        int discs;

        /** Cantidad de movimientos necesarios para resolver el juego. */
        int movements = 0;

        /** Lista de pasos necesarios para resolver el juego. */
        string steps = "";

        /** Indica si el juego ya fue resuelto. */
        bool solved = false;

        /**
         * Mueve los discos desde la torre inicial hasta la torre final,
         * utilizando una torre temporal cuando sea necesario.
         * @param num Cantidad de discos que se deben mover.
         * @param startPeg Torre de origen.
         * @param tempPeg Torre temporal.
         * @param endPeg Torre de destino.
         */
        void moveDiscs(int num, int startPeg, int tempPeg, int endPeg) 
        {
            if (num == 1) 
            {
                steps += "Mover un disco de la torre " +
                    to_string(startPeg) + " a la torre " +
                    to_string(endPeg) + "\n";
            }
            else 
            {
                moveDiscs(num - 1, startPeg, endPeg, tempPeg);

                steps += "Mover un disco de la torre " +
                    to_string(startPeg) + " a la torre " +
                    to_string(endPeg) + "\n";

                moveDiscs(num - 1, tempPeg, startPeg, endPeg);
            }

            movements++;
        }

    public:
        /**
         * Crea un juego con la cantidad de discos especificada.
         * @param discs Número de discos que se deben mover.
         */
        TowerOfHanoi(int discs) 
        {
            this->discs = discs;
        }

        /** Resuelve el juego moviendo todos los discos. */
        void solve() 
        {
            moveDiscs(discs, 1, 2, 3);
            solved = true;
        }

        /**
         * Devuelve la cantidad de movimientos necesarios para resolver el juego.
         * @return Número total de movimientos.
         */
        int getMovements() 
        {
            if (!solved)
                throw logic_error("El juego todavía no ha sido resuelto.");
            return movements;
        }

        /**
         * Devuelve la lista de pasos necesarios para resolver el juego.
         * @return Cadena con todos los movimientos realizados.
         */
        string getSteps() 
        {
            if (!solved)
                throw logic_error("El juego todavía no ha sido resuelto.");
            return steps;
        }
};