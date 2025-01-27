/*
 * University of Puerto Rico at Bayamón
 * Department of Computer Science
 * SICI 4036 - Data Structures, Spring 2021, Sec. KH1
 * File: EmptyCollectionException.java
 * Prof. Antonio F. Huertas
 */

package edu.uprb.datastructures;

/*
 * This is the exception thrown when trying to get an element 
 * from an empty collection.
 */
@SuppressWarnings("serial")
public class EmptyCollectionException extends RuntimeException 
{    
    /**
     * Creates an exception with no detail message.
     */
    public EmptyCollectionException() {
        super();
    }
    
    /**
     * Creates an exception with the given detail message.
     * @param msg
     */
    public EmptyCollectionException(String msg) {
        super(msg);
    }
}