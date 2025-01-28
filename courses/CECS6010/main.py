"""
Module Name: main.py
Description: The main menu for differents algorithms. 
Author: Cristian M. Pagan
Date: February 14, 2024
"""

# Module by analyzing sorting algorithms.
import sorting 
# Module by using binary exponentiation.
import binary_exponetiation as bin  
# Module by analyzing searching algorithms
import searching  
# Module implementing Horspool's algorithm.
import horspool  
# Module for analyzing recurrence.
import recurrences  

def main():
    while True:
        print("\nMenu:")
        print("1. Analyze Sorting Algorithms")
        print("2. Analyze Searching Algorithms")
        print("3. Determine order of growth for a given recurrence")
        print("4. Apply binary exponentation")
        print("5. Apply Horspool's algorithms")
        print("6. Exit")
        choice = input("Enter your choice: ")

        # Analyzing sorting algorithms...
        if choice == '1':
            sorting.main()
        # Analyze Searching Algorithms
        elif choice == '2':
            searching.main()
        # Determine order of growth for a given recurrence
        elif choice == '3':
            recurrences.main()
        # Apply binary exponentation
        elif choice == '4':
            bin.main()
        # Apply Horspool's algorithms
        elif choice == '5':
            horspool.main()
        # Exit the program.
        elif choice == '6':
            print("Exiting program. Goodbye!")
            break
        # Handle invalid menu choices
        else:
            print("Invalid choice! Please enter a valid option.")

if __name__ == "__main__":
    main()