/*
 * University of Puerto Rico at Bayamon
 * Department of Computer Science
 * COTI 3102 - Algorithms and Program Development II, Spring 2017, Section LR1
 * Prof. Lenis Torres-Berrios
 */

package edu.uprb.company;

import java.util.Scanner; // For the Scanner class
import java.io.*; // For file I/O classes

/**
 * This is a class reads a file and writes in file the ID, firstName, 
 * lastName, department and weekly salary of that employee.
 * @author Cristian M. Pagan {@literal <cristian.pagan3@upr.edu>}
 * @version 1.0
 * @since 16/05/2017
 */
public class EmployeePayroll 
{
	public static void main(String[] args)
	{
		// Create a Scanner object for keyboard input.
		Scanner keyboard = new Scanner(System.in);
		
		// Declare the variables for the Employee. 
		Department depart;
		String name, lastName;
		double payRate;
		int id, hours = 0; 
		
		// Get the name of the filename.
		System.out.print("Enter the filename: ");
		String inFile = keyboard.nextLine();
		
		// Calls setFile and inFile will be "employee.txt"
		inFile = setFile(inFile, "employee.txt");
		
		// Get the output filename.
		System.out.print("Enter the output filename: ");
		String outFile = keyboard.nextLine();
		
		// Calls setFile and outFile will be "payroll.txt"
		outFile = setFile(outFile, "payroll.txt");
		
		// Counter 
		int count = 0;
		
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
				depart = getDepart(inputFile.next()); 
				hours = inputFile.nextInt();
				payRate = inputFile.nextDouble(); 
				
				// Create an employees object, using constructor to validate data.
				Employee emp = new Employee(id, name, lastName, depart, hours, payRate);
				
				// Writes in the file id, name, lastName, department and salary.
				outputFile.println(emp);
				
				// Counts the employee written in the file.
				count++;
			}
			
			// Prints how many employee's were read and the name of the file written.
		    System.out.printf("\nAll %d employees were read.\n", count);
		    System.out.println("Results were written in " + outFile);
		    System.out.println();
		    
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
	
	/**
	 * Sets the file name to a give file or defaults to a specified 
	 * default if the given file does not have a .txt extension.
	 * @param file The file name provided by the user.
	 * @param defaultFile The default file name.
	 * @return The valid file name.
	 */
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
		/* Switch expression (Java 14) */
		return switch (department) {
			case "Finance" -> Department.FINA;
			case "Marketing" -> Department.MKTG;
			case "HR" -> Department.HMRS;
			case "IT" -> Department.INTE;
			case "Budget" -> Department.SALE;
			default -> Department.FINA;
		};	
	}
}
