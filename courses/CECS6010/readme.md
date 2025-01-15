# CECS 6010 - ADVANCED DESIGN AND ANALYSIS OF ALGORITHM
---

**Objective**: To understand of advanced algorithms methods, their concepts, 
and how they are used to engaging computational issues.

The **main.py** file provides a menu to select and explore different sorting 
algorithms. It allows users to visualize and understand how various 
sorting methods work by processing a given string.

1. **Analyze Sorting Algorithms**: This program analyzes sorting algorithms,
which are implemented in the file **sorting.py** for string.

* Sorting a word using Insertion Sort: chooses an element from the unsorted section
  iteratively and places it in the sorted section at the appropriate location.
* Sorting a word using Merge Sort: separates the word into smaller subwords,
  sorts them recursively, and then reassembles the subwords that have been sorted.
* Sorting a word using Quick Sort: After choosing a pivot element, divides the word
  into smaller and larger components and sorts each partition recursively.

2. **Analyze Searching Algorithms**: This program analyzes searching algortihms,
which are implemented in the file **searching.py** for integer numbers. 

* Analyze Binary Search with the average-case scenario: when there is an
  equal chance that the key element will appear anywhere in the sorted list.
* Analyze Binary Search with the worst-case scenario: when the
  important element is at the end of the sorted list or not present at all.
* Compare Binary Search vs. Sequential Search: When looking for an
  element in a list, this compares the speed and effectiveness of
  Binary Search and Sequential Search.

3. **Determine order of growth for a given recurrence**: Determines the order
   of growth for a given recurrence by accepting three integer inputs:
   a, b and d.
   
   *a*: A integer number positive greather than 1. <br>
   *b*: A integer number positive greather than 1. <br>
   *d*: A integer number positive greather than 1. <br>
   
   Since the inputs a, b, and d have been validate, we will apply the 
   **master theorem** which states:
   
   * If **a < b^d**: The time complexity is *Θ(n^d)*. 
   * If **a == b^d**: The time complexity is *Θ(n^d log n)*. 
   * If **a > b^d**: The time complexity is *Θ(n^(log_b a))*.

   Based on the recurrence, this figures out the asymptotic behavior of 
   recursive algorithms.

5. **Apply binary exponentation**: This program analyzes effective algorithm
   that uses binary representation to divide the exponentiation process into
   a number of smaller, more manageable steps in order to compute large powers
   of a number.

   The file **binary_exponentiation.py** contains implementations for binary
   exponentiation algorithms.
   
   * The **base** is set to 2 by default and must be a positive integer.
   * The **exponent** must be a positive integer.

   The program applies two (2) methods of binary exponentiation:
   
   * Left-to-right binary exponentiation: With this method, the exponentiation
   is calculated by looking at the exponent's bits from left to right.
   * Right-to-left binary exponentiation: With this method, the exponentiation
   is calculated by looking at the exponent's bits from right to left.

6. **Apply Horspool's algorithm to search words**: In the string search algorithm that
   effectively looks for a pattern in a text by calculating how much to shift
   the pattern upon a mismatch using a shift table.
   
   The required input to this function:
   * After the user enters a word or phrase (text), it is converted to uppercase
     for uniform comparison. For instance, you can try: "JIM_SAW_A_BARBERSHOP".
   * After the user enters a word (pattern), it is converted to uppercase
     for uniform comparison. For instance, you can try: "BARBER".

  7. **Apply Horspool's algorithm to search integers**: To search for integers we can
     interpret the binary pattern matching in the context of a binary string,
     where the pattern is a sequence of 1s and 0s in binary.

     The required input to this function:
     * After the user inputs a binary integer, the text is repeated by converting
       it to a string and multiplying it. For instance, you can try: "1000".
     * After the user inputs a binar pattern, the patter is search for in the
       binary string. For instance, you can try: "00001".

   8. **Exit**: This option allows you to exit the program.

**Solution:** This solution includes multiple Python files that implement various 
algorithms for solving problems related to sorting, searching, and exponentiation.
* [main.py](main.py)
* [binary_exponetiation.py](binary_exponetiation.py)
* [searching.py](searching.py)
* [sorting.py](sorting.py)
