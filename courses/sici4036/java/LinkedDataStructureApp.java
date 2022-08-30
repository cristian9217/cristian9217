/*
 * University of Puerto Rico at Bayamón
 * Department of Computer Science
 * SICI 4036 - Data Structures, Spring 2021, Sec. KH1
 * Prof. Antonio F. Huertas
 */

package edu.uprb.app;

import edu.uprb.datastructures.IntBinarySearchTree;
import edu.uprb.datastructures.IntLinkedQueue;
import edu.uprb.datastructures.IntLinkedStack;

/**
 * This is an application that demonstrates some methods 
 * of the Queue, Stack and Binary Search Tree (BST). 
 * @author Cristian M. Pagan {@literal <cristian.pagan3@upr.edu>}
 * @version 14/05/2021
 */
public class LinkedDataStructureApp 
{
	/**
     * Serves as the entry point for this application.
     * @param args Not applicable: The command-line arguments
     */
	public static void main(String[] args) 
	{
		double timeStack = timeStackPrint() / 1e6; 
		System.out.println("\nResult in miliseconds: " + timeStack);
		
		System.out.println();
		System.out.println("-----------------------------------------");
		
		double timeQueue = timeQueuePrint() / 1e6; 
		System.out.println("\nResult in miliseconds: " + timeQueue);
		
		System.out.println();
		System.out.println("-----------------------------------------");
		
		double timeBST = timeBSTPrint() / 1e6; 
		System.out.println("\nResult in miliseconds: " + timeBST);
		
		System.out.println();
		System.out.println("-----------------------------------------");
	}

	/**
     * Returns the time needed to run stack print.
     * @return The time in nanoseconds of execution of the methods.
     */
    private static long timeStackPrint() 
    {
        long startTime = System.nanoTime();
        stackPrint();
        return System.nanoTime() - startTime;
    }
	
    /**
     * This print the Stack algorithms with implementation.
     */
	private static void stackPrint() 
	{	
		IntLinkedStack stk = new IntLinkedStack();
		
		stk.push(2);
		stk.push(3);
		stk.push(4);
		stk.push(25);
		stk.push(5);
		stk.push(8);
		stk.push(8);
		stk.push(8);
		stk.push(7);

		System.out.println("Printing Integer Stack: " + stk);
		System.out.println("Amount of even numbers in stack is: " + 
						   	stk.countEven());
		System.out.println("Amount of odd numbers in stack is: " + 
				   		    stk.countOdd());
		System.out.println("The sum of the stack is: " + 
				   		    stk.sum());
		System.out.println("The sum of squares of the stack is: " + 
							stk.sumOfSquares());
		System.out.printf("The average of the stack is: %.2f", 
							stk.average());
		System.out.println("\nThe minimum of the stack is: " + 
							stk.minimum());
		System.out.println("The maximum of the stack is: " + 
							stk.maximum());
		
		int elem = 8;
		int index = stk.count(elem);
		
		if(index == 0)
			System.out.println("The " + elem + " it does not appear " + 
							   "in the stack.");
		else 
			System.out.println("The " + elem + " appears in the stack " + 
							   "at least " + index + ".");
		
		elem = 3;
		index = stk.linearSearch(elem);
		
		if(index < 0)
			System.out.println("The " + elem + " it does not appear " + 
					   		   "in the stack.");
		else
			System.out.println("The " + elem + " appears in the index " + 
							   "# " + index);
		
		elem = stk.pop();
		System.out.println("\nPop an element of the stack: " + elem);
		
		elem = stk.pop();
		System.out.println("Pop an element of the stack: " + elem);                                
		
		System.out.println("Printing Integer Stack: " + stk);
		System.out.println("The size of the stack after a " + 
						   "pop: " + stk.size());
	}
	
	/**
     * Returns the time needed to run queue print.
     * @return The time in nanoseconds of execution of the methods.
     */
    private static long timeQueuePrint() 
    {
        long startTime = System.nanoTime();
        queuePrint();
        return System.nanoTime() - startTime;
    }

    /**
     * This print the queue algorithms with implementation.
     */
	private static void queuePrint() 
	{
		IntLinkedQueue que = new IntLinkedQueue();
		
		que.add(36);
		que.add(47);
		que.add(41);
		que.add(58);
		que.add(77);
		que.add(77);
		que.add(77);
		que.add(83);
		
		System.out.println("Printing Integer Queue: " + que);
		System.out.println("Amount of even numbers in queue is: " + 
							que.countEven());
		System.out.println("Amount of odd numbers in queue is: " + 
				   		    que.countOdd());
		System.out.println("The sum of the queue is: " + 
				   		    que.sum());
		System.out.println("The sum of squares of the queue is: " + 
							que.sumOfSquares());
		System.out.printf("The average of the queue is: %.2f", 
							que.average());
		System.out.println("\nThe minimum of queue is: " + 
							que.minimum());
		System.out.println("The maximum of the queue is: " + 
							que.maximum());
		
		int elem = 77;
		int index = que.count(elem);
		
		if(index == 0)
			System.out.println("The " + elem + " it does not appear " + 
							   "in the queue.");
		else 
			System.out.println("The " + elem + " appears in the queue " + 
							   "at least " + index + ".");
		
		elem = 15;
		index = que.linearSearch(elem);
		
		if(index < 0)
			System.out.println("The " + elem + " it does not appear " + 
					   		   "in the queue.");
		else
			System.out.println("The " + elem + " appears in the index " + 
							   "# " + index);
		
		elem = que.remove();
		System.out.println("\nRemove an element of the queue: " + elem);
		
		elem = que.remove();
		System.out.println("Remove an element of the queue: " + elem);
		
		System.out.println("Printing Integer Queue: " + que);
		System.out.println("The size of the queue after a " + 
						   " pop: " + que.size());
	}
	
	/**
     * Returns the time needed to run binary search tree print.
     * @return The time in nanoseconds of execution of the methods.
     */
    private static long timeBSTPrint() 
    {
        long startTime = System.nanoTime();
        BSTPrint();
        return System.nanoTime() - startTime;
    }

    /**
     * This print the Binary Search Tree (<b>BST</b>) algorithms 
     * with implementation.
     */
	private static void BSTPrint() 
	{
		IntBinarySearchTree bst = new IntBinarySearchTree();
		
		bst.addRecursive(44);
		bst.addRecursive(20); 
		bst.addRecursive(10);
		bst.addRecursive(30);
		bst.addRecursive(50);
		bst.addRecursive(77);
		bst.addRecursive(80);
		bst.addRecursive(93);
		
		System.out.println("Printing Integer a tree: " + bst);
		System.out.println("Amount of even numbers in tree is: " + 
							bst.countEven());
		System.out.println("Amount of odd numbers in tree is: " + 
			   		    	bst.countOdd());
		System.out.println("The sum of the tree is: " + 
			   		    	bst.sumRecursive());
		System.out.println("The sum of squares of the tree is: " + 
							bst.sumOfSquares());
		System.out.printf("The average of the tree is: %.2f", 
							bst.averageRecursive());
		System.out.println("\nThe minimum of tree is: " + 
							bst.minimumIterative());
		System.out.println("The maximum of the tree is: " + 
							bst.maximumRecursive());
		
		int elem = 30;
		boolean found = bst.containsIterative(elem);
		
		if(!found)
			System.out.println("The " + elem + " it does not appear in the tree.");
		else
			System.out.println("The " + elem + " appears in the tree.");
		
		elem = 46;
		found = bst.containsRecursive(elem);
		
		if(!found)
			System.out.println("The " + elem + " it does not appear in the tree.");
		else
			System.out.println("The " + elem + " appears in the tree.");
		
		System.out.println("Inorder Tree: " + bst);
		System.out.println("PostOrder Tree: " + bst.toStringPostorder());
		System.out.println("PreOrder Tree: " + bst.toStringPreorder());
	}
}