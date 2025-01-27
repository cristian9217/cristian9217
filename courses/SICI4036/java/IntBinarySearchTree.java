/*
 * University of Puerto Rico at Bayamón
 * Department of Computer Science
 * SICI 4036 - Data Structures, Spring 2021, Sec. KH1
 * Prof. Antonio F. Huertas
 */

package edu.uprb.datastructures;

import java.util.NoSuchElementException;

/**
 * This is a class that represents a integer binary search tree.
 * @author Cristian M. Pagán {@literal <cristian.pagan3@upr.edu>}
 * @version 1.5
 * @since 14/05/2021
 */
public class IntBinarySearchTree implements IntBST
{
	/** Private class for a binary tree node */
	private Node root;
	
	/** Private class for a binary tree node */
	private static class Node 
	{
		/** The data of this node */
		public int data;
		
		/** The link to the node in the left subtree */
		public Node left;
		
		/** The link to the node in the right subtree */
		public Node right;
	}
	
	// Optional: Added to declare the root = null
	public IntBinarySearchTree() {
		root = null;
	}
	
	/** {@inheritDoc} */
	@Override
	public void addRecursive(int elem) {
		root = addRecursive(elem, root);
	}
	
	private Node addRecursive(int elem, Node curr) {
		if (curr == null) 
		{
			curr = new Node();
			curr.data = elem;
			curr.left = curr.right = null;
		}
	    
		else if (elem < curr.data)
	    	curr.left = addRecursive(elem, curr.left);
	    else if (elem > curr.data)
	    	curr.right = addRecursive(elem, curr.right);
	    else
	        curr.data = elem;  
		return curr;
	}
	
	/** {@inheritDoc} */
	@Override
	public boolean isEmpty() {
		return sizeRecursive() == 0;
	}
	
	/** {@inheritDoc} */
	@Override
	public int sizeRecursive() {
        return size(root);
    }

    private int size(Node curr) {
        if (curr == null)
            return 0;
        else
            return 1 + size(curr.left) + size(curr.right);
    }
    
    /** {@inheritDoc} */
	@Override
    public int depth() {
		Node curr = root;
		return depth(curr);
	}

	private int depth(Node curr)
	{
		if (curr == null)
			return 0;
		int leftDepth = depth(curr.left), rightDepth = depth(curr.right);

		if (leftDepth > rightDepth)
			return (leftDepth + 1);
		else
			return (rightDepth + 1);
	}
	
    /** {@inheritDoc} */
	@Override
    public int sumRecursive() {
        return sumElements(root);
    }

    private int sumElements(Node curr) {
        if (curr == null)
            return 0;
        else
            return curr.data + sumElements(curr.left) + sumElements(curr.right);
    }
	
    /** {@inheritDoc} */
   	@Override
    public double averageRecursive() 
    {
    	if(root == null)
    		throw new NoSuchElementException("empty tree");
    	return sumRecursive() / sizeRecursive();
    }
	
   	/** {@inheritDoc} */
   	@Override
	public int minimumIterative() {
        if (root == null)
            throw new NoSuchElementException("empty tree");
        Node trav = root;
        while(trav.left != null)
        	trav = trav.left;
        return trav.data;
    }
   	
   	/** {@inheritDoc} */
   	@Override
    public int minimumRecursive() {
        if (root == null)
            throw new NoSuchElementException("empty tree");
        return minimumRecursive(root);           
    }
    
    private int minimumRecursive(Node curr) {
        if (curr.left == null)
            return curr.data;
        else
            return minimumRecursive(curr.left);
    }
   	
    /** {@inheritDoc} */
   	@Override
	public int maximumIterative() {
        if (root == null)
            throw new NoSuchElementException("empty tree");
        Node trav = root;
        while(trav.right != null)
        	trav = trav.right;
        return trav.data;
    }
	
   	/** {@inheritDoc} */
   	@Override
    public int maximumRecursive() {
        if (root == null)
            throw new NoSuchElementException("empty tree");
        return maximumRecursive(root);           
    }
    
    private int maximumRecursive(Node curr) {
        if (curr.right == null)
            return curr.data;
        else
            return maximumRecursive(curr.right);
    }
    
    /** {@inheritDoc} */
   	@Override
	public boolean containsIterative(int elem) 
	{
   		if (root == null)
   			throw new NoSuchElementException("empty tree");
   		
   		Node trav = root;
		while (trav != null) 
		{
			if (trav.data == elem)
				return true;
			else 
				if (elem < trav.data)
					trav = trav.left;
				else
					trav = trav.right;
		}
		return false;
	}
   	
    /** {@inheritDoc} */
   	@Override
	public boolean containsRecursive(int elem) {
   		if (root == null)
   			throw new NoSuchElementException("empty tree");
   		return containsRecursive(elem, root);
	}
	
	private boolean containsRecursive(int elem, Node curr) {
	     if (curr == null)
	         return false;
	     else if (elem < curr.data)
	         return containsRecursive(elem, curr.left);
	     else if (elem > curr.data)
	         return containsRecursive(elem, curr.right);
	     else
	         return true;
	 }
	
   	/** {@inheritDoc} */
   	@Override
    public int sumOfSquares() {
     	if (root == null)
 			throw new NoSuchElementException("empty tree");
     	return sumOfSquares(root);
    }

    private int sumOfSquares(Node curr) {
     	if (curr == null)
 			return 0;
 		else
 			return (curr.data * curr.data) + 
 					sumOfSquares(curr.left) + 
 					sumOfSquares(curr.right);
    }
   	
	/** {@inheritDoc} */
   	@Override
	public int countEven() {
		if(root == null)
			throw new NoSuchElementException("empty tree");
		return countEven(root, 0);
	}
   	
   	private int countEven(Node curr, int count)
   	{
   		int temp = 0;
   		if(curr != null)  
   		{
   		 	count = countEven(curr.left, temp) + countEven(curr.right, temp);
   			if((curr.data % 2) == 0)
   				count++;
   		}
   		return count;
   	}
   	
   	/** {@inheritDoc} */
   	@Override
	public int countOdd() {
		if(root == null)
			throw new NoSuchElementException("empty tree");
		return countOdd(root, 0);
	}
   	
   	private int countOdd(Node curr, int count)
   	{
   		int temp = 0;
   		if(curr != null)  
   		{
   		 	count = countOdd(curr.left, temp) + countOdd(curr.right, temp);
   			if((curr.data % 2) != 0)
   				count++;
   		}
   		return count;
   	}
   	
   	
   	/** {@inheritDoc} */
   	@Override
    public String toString() {
   		if (root == null)
   			throw new NoSuchElementException("empty tree");
   		
   		StringBuilder str = new StringBuilder("[");
        treeInorder(root, str);
        return str.append("]").toString();      
    }

   	/** Inorder Tranversal */
    private void treeInorder(Node curr, StringBuilder str) {
        if (curr != null) 
        {
        	treeInorder(curr.left, str);
            if (curr.left != null) 
                str.append(", ");
            str.append(curr.data);
            if (curr.right != null)
                str.append(", ");
            treeInorder(curr.right, str);
        }
    }
    
    /** {@inheritDoc} */
   	@Override
    public String toStringPreorder() {
   		if (root == null)
   			throw new NoSuchElementException("empty tree");
   		
   		StringBuilder str = new StringBuilder("[");
        printPreorder(root, str);
        return str.append("]").toString();      
    }

   	/** Preorder Tranversal */
    private void printPreorder(Node curr, StringBuilder str) 
    {
        if (curr != null) 
        {
        	str.append(curr.data);
        	if(curr.left != null)
        		str.append(", "); 
        	printPreorder(curr.left, str);
        	if(curr.right != null)
        		str.append(", "); 
        	printPreorder(curr.right, str);
        }
    }
    
    /** {@inheritDoc} */
   	@Override
    public String toStringPostorder() {
   		if (root == null)
   			throw new NoSuchElementException("empty tree");
   		
   		StringBuilder str = new StringBuilder("[");
        printPostorder(root, str);
        return str.append("]").toString();      
    }

    private void printPostorder(Node curr, StringBuilder str) 
    {
        if (curr != null) 
        {
        	printPostorder(curr.left, str);
        	if(curr.left != null)
        		str.append(", ");
        	printPostorder(curr.right, str);
        	if(curr.right != null)
        		str.append(", "); 
        	str.append(curr.data); 
        }
    }	
}