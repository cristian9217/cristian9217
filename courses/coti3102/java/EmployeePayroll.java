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
	public static void main(String[] args)
	{
		// Create a Scanner object for keyboard input.
		Scanner keyboard = new Scanner(System.in);
		
		// Declare the variables. 
		String name, lastName;
		int count = 0, hours, id; double salary, payRate;
		
		// Get the name of the filename.
		System.out.print("Enter the filename: ");
		String inFile = keyboard.nextLine();
		
		inFile = setFile(inFile, "employee.txt");
		
		// Get the output filename.
		System.out.print("Enter the output filename: ");
		String outFile = keyboard.nextLine();
		
		outFile = setFile(outFile, "payroll.txt");
		
		try 
		{	
			// Open the file.
			File file = new File(inFile);
			Scanner inputFile = new Scanner(file);
			
			// Write the file.
			PrintWriter outputFile = new PrintWriter(outFile);
			
			// Read lines from the file until no more are left.
			while (inputFile.hasNext())
			{
				// Read the ID, firstName, lastName, department, hoursWorked, payRate. 
				id = inputFile.nextInt();
				name = inputFile.next();
				lastName = inputFile.next();
				Department depart = getDepart(inputFile.next()); 
				hours = inputFile.nextInt();
				payRate = inputFile.nextDouble(); 
				
				Employee emp = new Employee(id, name, lastName, depart, hours, payRate);

				// Calculates the weekly salary of that employee.
				salary = emp.weeklySalary();
				
				// Prints to the file id, name, lastName, department and salary.
				outputFile.println(id + "\t" + name + "\t" + lastName + "\t" + 
								   depart + "\t" + salary);
				
				// Counts the employee read and written in the file.
				count++;
			}
			
			// Prints how many employee's were read.
		    System.out.printf("\nAll %d employees were read.\n", count);
		    System.out.println("Results were written in " + outFile);
		    
		    // Close the file.
		    inputFile.close();
			outputFile.close();
		}
		catch(FileNotFoundException e)
		{
			System.out.println("File not found: " + e.getMessage());
		}
		finally 
		{
			// Close the keyboard.
			keyboard.close();
		}
	}
	
	
	public static String setFile(String file, String defaultFile)
	{
		if(!file.matches(".*\\.txt"))
		{
			System.out.println("Default filename: " + defaultFile);
			return defaultFile;
		}
		
		return file;
	}
	
	public static Department getDepart(String department)
	{
		switch(department)
		{
			case "Finance":			return Department.FINA;
			case "Marketing":		return Department.MKTG;
			case "HR":				return Department.HMRS;
			case "IT":				return Department.INTE;
			case "Budget":			return Department.SALE;
			default:				return Department.FINA;
		}		
	}
}
