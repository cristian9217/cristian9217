/*
 * University of Puerto Rico at Bayamón
 * Department of Computer Science
 * COTI 3101 - Algorithms and Program Development I, Spring 2017, Section LR1
 * Prof. Lenis Torres-Berrios
 */

package edu.uprb.company;

/**
 * This class represent an employee the ID, firstName, 
 * lastName, department and weekly salary of that employee.
 * @author Cristian M. Pagán {@literal <cristian.pagan3@upr.edu>}
 * @version 1.0
 * @since 14/05/2017
 */
public class Employee 
{
	///////////////////////////////////    Fields     ///////////////////////////////////
	
	/** The id for this employee */
	private final int id;
	
	/** The name of the employee */
	private String name;
	
	/** The last name of the employee */
	private String lastName; 
	
	/** The department from Enumeration */
	private Department department;
	
	/** The hours worked of the employee */
	private int hours;
	
	/** The pay rate of the employee */
	private double payRate;
	
	///////////////////////////////////  Constructors ///////////////////////////////////
	
	/** 
	 * Creates an Employee of ID, name, last name and department. 
	 * @param id The ID of the employee 
	 * @exception IllegalArgumentException if the ID is between 1000 and 9999.
	 * @param name The name of this employee
	 * @param lastName The last name of this employee
	 * @param department The department of this employee
	 */
	public Employee(int id, String name, String lastName, Department departament, 
					int hours, double payRate) 
	{	
		if(id < 1000 || id > 9999)
			throw new IllegalArgumentException("Invalid ID employee: " + id);
		else
			this.id = id;
		
		setName(name);
		setLastName(lastName);
		setDepartment(departament);
		this.setHours(hours);
		this.payRate = payRate;
	}
	
	/** 
	 * Creates an Employee with default constructor. 
	 * @param idEmployee The ID of an employee 
	 */
	public Employee(int id) {
		this(id, "John", "Doe", Department.FINA, 40, 8.25);
	}
	
	/////////////////////////////////// Instance Methods ///////////////////////////////////

	/**
	 * Returns the ID of this employee.
	 * @return The ID of this employee 
	 */
	public int getId() {
		return id;
	}

	/**
	 * Returns the name of this employee.
	 * @return The name of this employee 
	 */
	public String getName() {
		return name;
	}
	
	/** 
	 * Sets the first name of the employee to the given value. 
	 * @param name The name of this employee
	 * @exception IllegalArgumentException Validates the first name starts 
	 * with uppercase.
	 */
	public void setName(String name) 
	{
		if(!Character.isUpperCase(name.charAt(0)))
			die("First names starts with uppercase: " + lastName.charAt(0));
		
		if(name.length() < 2 || name.length() > 9)
			die("Your first name is too long or too short.");
		
		if(!name.matches("^[A-Z][a-z]{1,8}$"))
			die("Invalid first name: " + name);
		
		this.name = name;
	}

	/**
	 * Returns the last name of this employee.
	 * @return The last name of this employee.
	 */
	public String getLastName() {
		return lastName;
	}

	/**
	 * Sets the last name of the employee to the given value. 
	 * @param lastName The last name of this employee 
	 */
	public void setLastName(String lastName) 
	{
		if(!Character.isUpperCase(lastName.charAt(0)))
			die("Last names starts with uppercase: " + lastName.charAt(0));
		
		if(lastName.length() < 2 || lastName.length() > 9)
			die("Your last name is too long or too short.");
		
		if(!lastName.matches("^[A-Z][a-z]{1,8}$"))
			die("Invalid last name: " + lastName);
		
		this.lastName = lastName;
	}

	/**
	* Returns the department of the employee.
	* @return The department of the enum class.
	*/
	public Department getDepartment() {
		return department;
	}

	/**
	 * Sets the department of the enum of the department to the given value.
	 * @param department The department from the <b>enum</b>. 
	 */
	public void setDepartment(Department department) {
		this.department = department;
	}

	/**
	* Returns the hours of this employee.
	* @return The hours of this employee.
	*/
	public int getHours() {
		return hours;
	}
	
	/**
	 * Sets the hours of the employee to the given value.
	 * @param hours the hours of the employee.
	 * @throws IllegalArgumentException if the hours are less than 0 or more than 60
	 */
	public void setHours(int hours) 
	{
		if(hours < 0 || hours > 60)
			die("Invalid hours worked: " + hours);
		this.hours = hours;
	}

	
	/**
	 * Returns the pay rate of the employee
	 * @return pay rate of the employee
	 */
	public double getPayRate() {
		return payRate;
	}
	
	/**
	 * Sets the pay rate of the employee to the given value.
	 * @param payRate the pay rate by the employee.
	 * @throws IllegalArgumentException if the pay rate are less than 7 or more than 50
	 */
	public void setPayRate(double payRate) 
	{
		if(payRate < 7.00 || payRate > 50.00)
			die("Invalid pay rate: " + payRate);
		this.payRate = payRate;
	}
		
	/**
	 * Calculates the weekly salary of the employee.
	 * @return The weekly salary of the employee.
	 */
	public double weeklySalary() 
	{
		// If the number of hours worked is greater than 40.
		// If overtime rate of 1.5 should be applied.
		final double REGULAR_HOURS = 40.0;
		final double OVERTIME = 1.5;
		
		if(hours <= REGULAR_HOURS)
			return hours * payRate;
		else 
			return (REGULAR_HOURS * payRate) + ((hours - REGULAR_HOURS) * OVERTIME * payRate);
	}
	
	///////////////////////////////////  Class Methods ///////////////////////////////////
	
	/**
	 * Displays an error message
	 * @param message Defines an error message
	 */
	private void die(String message) {
		throw new IllegalArgumentException(message);
	}
}
