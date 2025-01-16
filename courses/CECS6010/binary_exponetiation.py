"""
Module Name: binary_exponentiation.py
Description: A Python module implementing left-to-right 
and right-to-left binary exponentiation techniques.
Author: Cristian M. Pagan
Date: February 14, 2024
"""

class BinaryExponentiation: 
    """
        A class to perform binary exponentiation using 
        left-to-right and right-to-left methods.
    
        Attributes:
            a (int): The base of the exponentiation (default is 2).
            n (int): The exponent (default is 17).
    """
    def __init__(self, a = 2, n = 17):
        """ Intializes the BinaryExponetiation. """
        if a <= 0:
            raise ValueError("Base must be positive.")
        if n <= 0:
            raise ValueError("Exponent must be positive.")
        
        self.a = a
        self.n = n

    def left_right_binary_exponentiation(self):
        """ Performs left-to-right binary exponentiation. """
        binary_n = bin(self.n)[self.a:] 
        print(f"n = {self.n} = ({binary_n})_2")
        self.process_binary_exponentiation(binary_n)

    def right_left_binary_exponentiation(self):
        """ Performs right-to-left binary exponentiation. """
        binary_n = bin(self.n)[self.a:] 
        print(f"n = {self.n} = ({binary_n})_2")
        binary_n = binary_n[::-1]
        self.process_binary_exponentiation(binary_n)

    def process_binary_exponentiation(self, binary_n):
        """ Process binary exponentiation steps. """
        for i, bit in enumerate(binary_n):
            if bit == '1':
                if(i == 0):
                    print(f"1 = a")
                else:
                    print(f"1 = a^{2 ** i} * a")
            else:
                print(f"0 = a^{2 ** i}")

    def __str__(self):
        return f"The base is {self.a} and exponent {self.n}"

def main():
    """ Provides a menu for selecting the exponetiation method. """
    while True: 
        # Displaying the menu options for the user
        print("\nMenu of Binary Exponetiation:")
        print("1. Return to the Main Menu")
        print("2. Apply left-to-right binary exponentation")
        print("3. Apply right-to-left binary exponentation")
        choice = input("Enter your choice: ")
        
        # Return to the Main Menu.
        if choice == '1':
            return
        # Apply the left-to-right binary exponentation.
        elif choice == '2':
            try:
                num = int(input("Enter the number n: "))

                binaryLeft = BinaryExponentiation(n = num)
                print(str(binaryLeft))
                binaryLeft.left_right_binary_exponentiation()
            except ValueError as e:
                print(f"Invalid input! {e}")    
        # Apply the right-to-left binary exponentation.
        elif choice == '3':
            try:
                num = int(input("Enter the number n: "))

                binaryRight = BinaryExponentiation(n = num)
                print(str(binaryRight))
                binaryRight.right_left_binary_exponentiation()
            except ValueError as e:
                print(f"Invalid input! {e}")    
        # When user do not select the right option.
        else:
            print("Invalid choice! Please enter a valid option.")
