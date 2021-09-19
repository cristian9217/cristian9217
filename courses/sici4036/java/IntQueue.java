/*
 * University of Puerto Rico at Bayamón
 * Department of Computer Science
 * SICI 4036 - Data Structures, Fall 2020, Sec. KR1
 * Prof. Antonio F. Huertas
 */

package edu.uprb.datastructures;

/**
 * This interface represents a integer queue.
 * @author Cristian M. Pagán {@literal <cristian.pagan3@upr.edu>}
 * @version 1.3
 * @since 05/12/2020
 */
public interface IntQueue 
{
	/**
	 * Pushes an element into the stack
	 * @param elem An integer number element
	 */
	void add(int elem);
		
	/**
	  * Pops an element from the stack. This method
	  * does remove the element from the stack.
	  * @return pops element from the stack.
	  */
	int remove();
		
	/**
	 * Peeks the top element from the stack. This method
	 * does not removes the top element from the stack.
	 * @return top element from the stack.
	 */
	int peek();
		
	/**
	 * Checks if the stack is empty
	 * @return {@code true} if the stack has no elements
	 * <br> {@code false} if the stack has elements.
	 */
	boolean isEmpty();
		
	/**
	 * Returns the amount of elements inside the stack
	 * @return the size in the stack
	 */
	int size();
		
	/** 
	 * Returns the sum of the elements inside the stack.
	 * @return the sum in the stack
	 */
	int sum();
	
	/**
	 * Returns the average of the elements inside the stack.
	 * @return The sum divide by the size in the stack.
	 */
	double average();
	
	/**
	 * Returns the minimum of the elements inside the stack.
	 * @return the smallest element in the stack.
	 */
	int minimum();
	
	/**
	 * Returns the maximum of the elements inside the stack.
	 * @return the largest element in the stack.
	 */
	int maximum();
	
	/**
	 * Searches for an element in the stack. 
	 * @param elem An integer number element 
	 * @return the position element in the stack.
	 */
	int linearSearch(int elem);
	
	/**
	 * Returns the sum of the elements by the power of 2.
	 * @return the sum of squares in the stack.
	 */
	int sumOfSquares();
	
	/**
	 * Counts the specified elem in the stack.
	 * @param elem An integer number element 
	 * @return counts the amount of elements in the stack.
	 */
	int count(int elem);
	
	/**
	 * Counts the even numbers can be divisible by two. 
	 * <br> Example: {2, 4, 6, 8, 10, ...}
	 * @return counts the amount of even elements.
	 */
	int countEven();
	
	/**
	 * Counts the odd numbers cannot be divisible by two. 
	 * <br> Example: {1, 3, 5, 7, 9, ...}
	 * @return counts the amount of odd elements. 
	 */
	int countOdd();
	
	/**
	 * Returns a string representation of the contents of the stack
	 * @return String representation of the contents of the stack
	 */
	String toString();
		
}