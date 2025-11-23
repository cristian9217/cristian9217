/*
 * File: RoofCost.java
 * Course: COTI-3101-LR1 
 * Date: April 11, 2018
 * Purpose: Calculates the area of a roof and estimates 
 * the cost according to three different rates.
 */

import java.util.Scanner;

/**
 * Calculates the area of a roof and estimates the cost 
 * according to three different rates. Includes methods 
 * to calculate the area and the price of the roof.
 * @author Cristian Pagán
 * @version 04/11/2018
 */
public class RoofCost 
{
    /**
     * Calculates the area of the roof.
     * @param width Width of the roof in meters.
     * @param length Length of the roof in meters.
     * @return Area of the roof.
     */
    public static double getArea(double ancho, double largo)
    {
        return (ancho * largo) / 9; 
    }
    
    /**
     * Calculates the price of the roof based on a rate index.
     * @param area Area of the roof.
     * @return Price calculated according to the selected rate.
     */
    public static double getPrecio(int index, double area)
    {
        double precio[] = {8, 16, 24}; 
        return precio[index] * area; 
    }
    
    /**
     * Serves as the entry point for this application.
     * @param args Not applicable: The command-line arguments
     */
    public static void main(String[] args)
    {
        // Scanner to read user input
        Scanner kbd = new Scanner(System.in); 
        
        System.out.print("Indique el ancho del techo: ");
        double ancho = kbd.nextDouble();
        
        System.out.print("Indique el largo del techo: ");
        double largo = kbd.nextDouble();
        
        // Calculate the area using the getArea method
        double area = getArea(ancho, largo);
        
        // Display costs according to the three rates
        System.out.printf("\nCosto #1: $%,.2f", getPrecio(0, area));
        System.out.printf("\nCosto #2: $%,.2f", getPrecio(1, area));
        System.out.printf("\nCosto #3: $%,.2f", getPrecio(2, area));
        
       	// Close the scanner
        kbd.close();
    }
}
