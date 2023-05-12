/*
 * University of Puerto Rico at Bayamón
 * Department of Computer Science
 * COTI 3101 - Algorithms and Program Development I, Spring 2017, Section LR1
 * Prof. Lenis Torres-Berrios
 */

package edu.uprb.company;

import java.util.Scanner; // For the Scanner class
import java.io.*; // For file I/O classes

/**
 * This is a class reads a file and writes in file the ID, firstName, 
 * lastName, department and weekly salary of that employee.
 * @author Cristian M. Pagán {@literal <cristian.pagan3@upr.edu>}
 * @version 1.0
 * @since 16/05/2017
 */
public class EmployeePayroll 
{
	public static void main(String[] args) throws IOException
	{
		// Create a Scanner object for keyboard input.
		Scanner keyboard = new Scanner(System.in);
		
		// Declare the variables. 
		String inFile, id, name, lastName, department, outFile = null;
		int count = 0, hours;
		double salary, payRate;
		
		// Get the name of the filename.
		System.out.print("Enter the filename: ");
		inFile = keyboard.nextLine();
		
		// Get the output filename.
		System.out.print("Enter the output filename: ");
		outFile = keyboard.nextLine();
		
		// Open the file.
		File file = new File(inFile);
		Scanner inputFile = new Scanner(file);
		
		// Write the file.
		PrintWriter outputFile = new PrintWriter(outFile);
		
		// Read lines from the file until no more are left.
		while (inputFile.hasNext())
		{
			// Read the ID, firstName, lastName, department, hoursWorked, payRate. 
			id = inputFile.next();
			name = inputFile.next();
			lastName = inputFile.next();
			department = inputFile.next();
			hours = inputFile.nextInt();
			payRate = inputFile.nextDouble(); 

			// Calculates the weekly salary of that employee.
			salary = weeklySalary(hours, payRate);
			
			// Prints to the file id, name, lastName, department and salary.
			outputFile.println(id + "\t" + name + "\t" + lastName + "\t" + 
							   department + "\t" + salary);
			
			// Counts the employee read and written in the file.
			count++;
		}
		
		// Prints how many employee's were read.
	    	System.out.printf("\nAll %d employees were read.\n", count);
	    	System.out.println("Results were written in " + outFile);
		
		// Close the file and keyboard.
		keyboard.close();
		inputFile.close();
		outputFile.close();
	}

	/**
	 * Calculates the weekly salary of the employee.
	 * @param hours The hours worked of the employee.
	 * @param payRate The pay rate of the employee.
	 * @return The weekly salary of the employee.
	 */
	public static double weeklySalary(int hours, double payRate) 
	{
		final int REGULAR_HOURS = 40;
		
		if(hours <= REGULAR_HOURS)
			return hours * payRate;
		else 
			return payRate * REGULAR_HOURS + ((hours - REGULAR_HOURS) * payRate * 1.5);
	}
}
