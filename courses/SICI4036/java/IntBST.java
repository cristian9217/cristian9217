/*
 * University of Puerto Rico at Bayamón
 * Department of Computer Science
 * SICI 4036 - Data Structures, Fall 2020, Sec. KR1
 * Prof. Antonio F. Huertas
 */

package edu.uprb.datastructures;

/**
 * This interface represents a integer binary tree search.
 * @author Cristian M. Pagán {@literal <cristian.pagan3@upr.edu>}
 * @version 1.3
 * @since 04/12/2020
 */
public interface IntBST 
{
	/**
	 * Inserts recursive an element into the tree and
	 * returns a reference to its root.
	 * @param elem The element to be inserted in the tree.
	 */
	void addRecursive(int elem);
		
	/**
	 * Checks if the binary search tree <b>(BST)</b> is empty
	 * @return {@code true} if the <b>(BST)</b> has no elements
	 * <br> {@code false} if the <b>(BST)</b> has elements.
	 */
	boolean isEmpty();
		
	/**
	 * Returns the size recursive of the elements in this tree.
	 * @return The size of the elements in this tree.
	 */
	int sizeRecursive();
	
	/**
     * Returns the depth of the elements in this tree. 
     * @return The depth of elements on this tree. 
     */
	int depth();
	
	 /**
     * Returns the sum recursive of the elements in this tree.
     * @return The sum of the elements in this tree.
     */
	int sumRecursive();
	
	/**
     * Returns the average recursive of the elements in this tree.
     * @return The average of the elements in this tree
     */
	double averageRecursive();
	
	/**
     * Returns the minimum iterative of the elements in this tree.
     * @return The minimum of the elements in this tree.
     */
	int minimumIterative();
	
	/**
     * Returns the minimum recursive of the elements in this tree.
     * @return The minimum of the elements in this tree.
     */
	int minimumRecursive();
	
	/**
     * Returns the maximum iterative of the elements in this tree.
     * @return The maximum of the elements in this tree.
     */
	int maximumIterative();
	
	/**
     * Returns the maximum recursive of the elements in this tree.
     * @return The maximum of the elements in this tree.
     */
	int maximumRecursive();
	
	/**
	 * Returns if the element contains iterative the element in the tree.
	 * @param elem The element to be evaluated.
	 * @return {@code True} if the element was found returns true. <br>
	 *         {@code False} if the element was not found returns false.
	 */
	boolean containsIterative(int elem);
	
	/**
	 * Returns if the element contains the element in the tree.
	 * @param elem The element to be evaluated.
	 * @return {@code True} if the element was found returns true. <br>
	 *         {@code False} if the element was not found returns false.
	 */
	boolean containsRecursive(int elem);
	
	/**
	 * Returns the sum of the elements by the power of 2.
	 * @return the sum of squares in the binary search tree.
	 */
	int sumOfSquares();
	
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
     * NOTE: Prints the tree Inorder Traversal. <br>
     * Returns a string representation of this tree in inorder.
     * @return The string representation of this tree
     */
	String toString();
	
	/**
     * NOTE: Prints the tree Preorder Traversal. <br>
     * Returns a string representation of this tree in preorder.
     * @return The string representation of this tree
     */
	String toStringPreorder();
	
	/**
     * NOTE: Prints the tree Postorder Traversal. <br>
     * Returns a string representation of this tree in postorder.
     * @return The string representation of this tree
     */
	String toStringPostorder();
		
}