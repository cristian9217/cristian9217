"""
Module Name: recurrences.py
Description: A Python module implementing 
recurrences using Master Theorem.
Author: Cristian M. Pagan
Date: February 14, 2024
"""

import math

class Recurrences:
    """
    A class to handle recurrences based on 
    given numbers a, b, and d.
    
    Attributes:
        a (int): The value of a.
        b (int): The value of b.
        d (int): The value of d.
    """
    def __init__(self, a, b, d):
        """Initializes the class with a, b, and d."""
        self.a = self.set_number('a', a)
        self.b = self.set_number('b', b)
        self.d = self.set_number('d', d)
    
    def set_number(self, var_name, num):
        """Sets the number after validating that it is greater than 0."""
        try: 
            num = int(num)
            if num < 1: raise TypeError
        except ValueError:
            raise ValueError(f"{var_name} must be an integer.")
        except TypeError:
            raise TypeError(f"{var_name} must be >= 1.")
        
        return num
            
    def recurrences(self):
        """Returns the recurrence based on the values of a, b, and d."""
        a, b, d = self.a, self.b, self.d
        
        if a > (b**d):
            result = round(math.log(a, b))
            return f"a > b^d, O(n^log({a}, {b})) = O(n^{result})"
        elif a == (b**d):
            return f"a = b^d, O(n^{d} log n)"
        else:
            return f"a < b^d, O(n^{d})"
    
    def __str__(self):
        """Returns a string representation of the Recurrences."""
        return f"a = {self.a}, b = {self.b}, d = {self.d}"

def main():  
    while True:
        print("\nMenu of Recurrences:")
        print("1. Return to the Main Menu")
        print("2. Determine order of growth")
        choice = input("Enter your choice: ")
        
        # Return to the Main Menu.
        if choice == '1':
            return
        # Determine the order of growth.
        elif choice == '2':
            try:
                # Get inputs from the user
                a = input("Enter the number a: ") 
                b = input("Enter the number b: ")
                d = input("Enter the number d: ")

                # Create an instance of the Recurrences
                r = Recurrences(a, b, d)
                
                # Print the results.
                print(f"{r}. Since {r.recurrences()}")
            except ValueError as e:
                print(f"Invalid input! {e}")
            except TypeError as e:
                print(f"Number {e}")
        else:
            print("Invalid choice! Please enter a valid option.")
