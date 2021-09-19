/*
 * University of Puerto Rico at Bayamón
 * Department of Computer Science
 * SICI 4036 - Data Structures, Fall 2020, Sec. KR1
 * Prof. Antonio F. Huertas
 */

package edu.uprb.datastructures;

/**
 * This is a class that represent Stack with implementation of Linked List.
 * @author Cristian M. Pagán {@literal <cristian.pagan3@upr.edu>}
 * @version 1.3
 * @since 04/12/2020
 */
public class IntLinkedStack implements IntStack
{
	/** Reference to the first node in the list */
	private Node head;
	
	/** The length of the stack for the linked list */
	private int size;
	
	/**
	 * <b> A constructor is not necessarily this default 
	 * constructor for the stack. </b>
	 */
	public IntLinkedStack() 
	{ 
		head = null;
		size = 0;
	}
	
	/** {@inheritDoc} */
	@Override
	public void push(int elem) 
	{
		head = new Node(elem, head);
		size++;
	}
	
	/** {@inheritDoc} */
	@Override
	public int pop() 
	{
		if (isEmpty())
			throw new EmptyCollectionException("empty stack");
		
		int elem = head.data;
		head = head.next;
		size--;
		
		return elem;
	}

	/** {@inheritDoc} */
	@Override
	public int peek() 
	{
		if (isEmpty())
			throw new EmptyCollectionException("empty stack");
		return head.data;
	}

	/** {@inheritDoc} */
	@Override
	public int sum() 
	{
		int sum = 0;
		for (Node curr = head; curr != null; curr = curr.next)
			sum += curr.data;
		return sum;
	}
	
	/** {@inheritDoc} */
	@Override
	public double average() {
		return sum() / size(); // Alt. sum() / size; 
	}

	/** {@inheritDoc} */
	@Override
	public int minimum() 
	{
		// Has the first element of the stack.
		int min = head.data;
		
		for (Node curr = head.next; curr != null; curr = curr.next) 
			if (curr.data < min)
				min = curr.data;
		return min;
	}

	/** {@inheritDoc} */
	@Override
	public int maximum() 
	{
		// Has the first element of the stack.
		int max = head.data;
		
		for (Node curr = head.next; curr != null; curr = curr.next) 
			if (curr.data > max)
				max = curr.data;
		
		return max;
	}
	
	/** {@inheritDoc} */
	@Override
	public int size() 
	{		
		return size; 
	}
	
	/** {@inheritDoc} */
	@Override
	public boolean isEmpty() 
	{ 
		return (head == null); 
	}
	
	/** {@inheritDoc} */
	@Override
	public int linearSearch(int elem) 
	{
		 int pos = 0;
	     for (Node curr = head; curr != null; curr = curr.next)
	    	 if (elem == curr.data)
	    		 return pos;
	    	 else
	    		 pos++;
	     return -1;
	}

	/** {@inheritDoc} */
	@Override
	public int sumOfSquares() 
	{
		int sum = 0;
		for(Node curr = head; curr != null; curr = curr.next)
			sum +=  curr.data * curr.data;
		return sum;
	}

	/** {@inheritDoc} */
	@Override
	public int count(int elem) 
	{
		int count = 0;
		for(Node curr = head; curr != null; curr = curr.next)
			if(elem == curr.data)
				count++;
		return count;
	}
	
	/** {@inheritDoc} */
	@Override
	public int countEven() {
		int countEven = 0;
		for(Node curr = head; curr != null; curr = curr.next)
			if(curr.data % 2 == 0)
				countEven++;
		return countEven;
	}

	/** {@inheritDoc} */
	@Override
	public int countOdd() {
		int countOdd = 0;
		for(Node curr = head; curr != null; curr = curr.next)
			if(curr.data % 2 != 0)
				countOdd++;
		return countOdd;
	}

	/** {@inheritDoc} */
	@Override
	public String toString() 
	{
		StringBuilder strBld = new StringBuilder("[");
		for (Node trav = head; trav != null; trav = trav.next) 
		{
			strBld.append(trav.data);
			if (trav.next != null)
				strBld.append(", ");
		}
		strBld.append("]");
		return strBld.toString();
	}
	
	/** Reference to the first node in the list */
	private static class Node
	{
		/** The data of this node. */
        public int data;
        
        /** The link to the next node. */
        public Node next;
		
        /**
         * Creates a node with the given data and next link.
         * @param data The data of this node
         * @param next The link to the next node.
         */
		public Node(int elem, Node refNode) 
		{
			data = elem;
			next = refNode;
		}
	}
}