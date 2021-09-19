/*
 * University of Puerto Rico at Bayamón
 * Department of Computer Science
 * SICI 4036 - Data Structures, Fall 2020, Sec. KR1
 * Prof. Antonio F. Huertas
 */

package edu.uprb.datastructures;

/**
 * This is a class that represent Queue with implementation of Linked List.
 * @author Cristian M. Pagán {@literal <cristian.pagan3@upr.edu>}
 * @version 1.3
 * @since 05/12/2020
 */
public class IntLinkedQueue implements IntQueue
{
    /** The reference to the front node of this queue. */
	private Node front;
	
	/** The reference to the rear node of this queue. */
    private Node rear;
    
    /** The length of the queue for the linked list */
    private int size;
    
    /**
	 * <b> A constructor is not necessarily this default 
	 * constructor for the queue. </b>
	 */
    public IntLinkedQueue() 
    {
        front = rear = null;
        size = 0;
    }

    /** {@inheritDoc} */
    @Override
    public void add(int elem) 
    {
        if (front == null)
            front = rear = new Node(elem);
        else
            rear = rear.next = new Node(elem);
        size++;
    }

    /** {@inheritDoc} */
    @Override
    public int remove() 
    {
        if (isEmpty())
            throw new EmptyCollectionException("Empty queue");
        int elem = front.data;
        front = front.next;
        if (front == null)
            rear = null;
        size--;
        return elem;
    }

    /** {@inheritDoc} */
    @Override
    public int peek() 
    {
        if (isEmpty())
            throw new EmptyCollectionException("empty queue");
        return front.data;
    }

    /** {@inheritDoc} */
    @Override
    public boolean isEmpty() {
        return size == 0;
    }

    /** {@inheritDoc} */
    @Override
    public int size() {
        return size;
    }

    /** {@inheritDoc} */
    @Override
    public int sum() 
    {
    	int sum = 0;
		for (Node curr = front; curr != null; curr = curr.next)
			sum += curr.data;
		return sum;
    }
    
    /** {@inheritDoc} */
	@Override
	public double average() {
		return sum() / size; // Alt. sum() / size(); 
	}

	/** {@inheritDoc} */
	@Override
	public int minimum() 
	{
		// Has the first element of the stack.
		int min = front.data;
		
		for (Node curr = front.next; curr != null; curr = curr.next) 
			if (curr.data < min)
				min = curr.data;
		return min;
	}

	/** {@inheritDoc} */
	@Override
	public int maximum() 
	{
		// Has the first element of the stack.
		int max = front.data;
		
		for (Node curr = front.next; curr != null; curr = curr.next) 
			if (curr.data > max)
				max = curr.data;
		
		return max;
	}
    
    /** {@inheritDoc} */
    @Override
    public String toString() {
        StringBuilder str = new StringBuilder("[");
        for (Node curr = front; curr != null; curr = curr.next) {
            str.append(curr.data);
            if (curr.next != null)
                str.append(", ");
        }
        return str.append("]").toString();
    }

    /** {@inheritDoc} */
	@Override
	public int linearSearch(int elem) {
		 int pos = 0;
	     for (Node curr = front; curr != null; curr = curr.next)
	    	 if (elem == curr.data)
	    		 return pos;
	    	 else
	    		 pos++;
	     return -1;
	}

	 /** {@inheritDoc} */
	@Override
	public int sumOfSquares() {
		int sum = 0;
		for (Node curr = front; curr != null; curr = curr.next)
			sum += curr.data * curr.data;
		return sum;
	}

	/** {@inheritDoc} */
	@Override
	public int count(int elem) {
		int count = 0;
		for(Node curr = front; curr != null; curr = curr.next)
			if(curr.data == elem)
				count++;
		return count;
	}

	 /** {@inheritDoc} */
	@Override
	public int countEven() {
		int count = 0;
		for(Node curr = front; curr != null; curr = curr.next)
			if(curr.data % 2 == 0)
				count++;
		return count;
	}

	/** {@inheritDoc} */
	@Override
	public int countOdd() {
		int count = 0;
		for(Node curr = front; curr != null; curr = curr.next)
			if(curr.data % 2 != 0)
				count++;
		return count;
	}
	
	/** This private static class implements a linked list node. */
	private static class Node
	{
		/** The data of this node. */
		public int data;
		
		/** The link to the next node. */
		public Node next;
		
		/**
         * Creates a node with the given data.
         * @param data The data of this node
         */
		public Node(int elem) 
		{
			data = elem;
		}
	}
}
