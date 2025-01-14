/*
 * University of Puerto Rico at Bayamon
 * Department of Computer Science
 * COTI 3102 - Algorithms and Program Development II, Spring 2017, Section LR1
 * Prof. Lenis Torres-Berrios
 */

package edu.uprb.company;

/**
 * This is an interface represents different departments.
 * @author Cristian M. Pagán {@literal <cristian.pagan3@upr.edu>}
 * @version 1.0
 * @since 14/05/2017
 */
public enum Department 
{
	/** The name of the department of Finance */
	FINA, 
	
	/** The name of the department of Marketing */
	MKTG, 
	
	/** The name of the department of Human Resources */
	HMRS, 
	
	/** The name of the department of Information Technology */
	INTE,
	
	/** The name of the department of Sales */
	SALE;
	
	/**
     * Returns the string representation of the department.
     * @return The string representation of the department. 
     */
	@Override
	public String toString() 
	{
		/* Switch expression (Java 14) */
		return switch (this) {
			case FINA -> "Finance";
			case MKTG -> "Marketing";
			case HMRS -> "HR";
			case INTE -> "IT";
			case SALE -> "Budget";
			default -> "Finance";
		};
	}
}
