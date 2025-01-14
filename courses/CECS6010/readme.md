# CECS 6010 - ADVANCED DESIGN AND ANALYSIS OF ALGORITHM

The **main.py** file provides a menu to select and explore different sorting 
algorithms. It allows users to visualize and understand how various 
sorting methods work by processing a given string.

1. This program analyzes sorting algorithms, showing the process of sorting a 
string step by step. The core implementation of these algorithms is 
contained in the file **sorting.py**.

* Sorting a word using Insertion Sort: chooses an element from the unsorted section
  iteratively and places it in the sorted section at the appropriate location.
* Sorting a word using Merge Sort: separates the word into smaller subwords,
  sorts them recursively, and then reassembles the subwords that have been sorted.
* Sorting a word using Quick Sort: After choosing a pivot element, divides the word
  into smaller and larger components and sorts each partition recursively.

1. This program analyzes searching algortihms, which are implemented in the 
file **searching.py** for integer numbers. 

* Analyze Binary Search with the average-case scenario: when there is an
  equal chance that the key element will appear anywhere in the sorted list.
* Analyze Binary Search with the worst-case scenario: when the
  important element is at the end of the sorted list or not present at all.
* Compare Binary Search vs. Sequential Search: When looking for an
  element in a list, this compares the speed and effectiveness of
  Binary Search and Sequential Search.

1. Determines the order of growth for a givebn recurrence by accepting three
   integer inputs: a, b and d. 
   *a*: A integer number positive greather than 1.
   *b*: A integer number positive greather than 1.
   *d*: A integer number positive greather than 1.
   
  Since the inputs a, b, and d have been validate, we will apply the 
  **master theorem** which states:

  If a < b^d: The time complexity is Θ(n^d). 
  If a == b^d: The time complexity is Θ(n^d log n). 
  If a > b^d: The time complexity is Θ(n^(log_b a))

  Based on the recurrence, this figures out the asymptotic behavior of 
  recursive algorithms.

1. This program analyzes effective algorithm that uses binary representation
   to divide the exponentiation process into a number of smaller, more
   manageable steps in order to compute large powers of a number.

   The file **binary_exponentiation.py** contains implementations for binary
   exponentiation algorithms.
   * The **base** is set to 2 by default and must be a positive integer.
   * The **exponent** must be a positive integer.

   The program applies two (2) methods of binary exponentiation:
   * Left-to-right binary exponentiation: With this method, the exponentiation
   is calculated by looking at the exponent's bits from left to right.
   * Right-to-left binary exponentiation: With this method, the exponentiation
   is calculated by looking at the exponent's bits from right to left.
   

   
  
  
  

   
   
