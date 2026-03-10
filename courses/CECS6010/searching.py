"""
    Module Name: searching.py
    Description: A Python module implementing searching 
    algorithms such as Binary Search for average case, 
    worst case adn comparing linear and binary search. 
    Author: Cristian M. Pagan
    Date: February 14, 2024
"""

import math
import time

class ArraySearching:
    """
    A class to implement various search algorithms like
    Binary Search, with average and worst-case analysis.
    
    Attributes:
        arr (list): The list of numbers.
        length (int): The length of the array.
    """
    def __init__(self, arr):
        """ Initializes the ArraySearching class with the given array."""        
        self.setArray(arr)
        self.setLength()

    def setArray(self, arr):
        """ Sets the array filtering out negatives values. """
        if len(arr) == 0:
            arr = [3, 14, 27, 31, 39, 42, 55, 70, 74, 81, 85, 93, 98]
        else:
            arr = sorted([x for x in arr if x >= 0])
        self.arr = arr

    def setLength(self):
        """ Sets the length of the array."""
        self.length = len(self.arr)
        
    # Performing Binary Search with average-case
    def average_binary_search(self):
        """ 
        Performs Binary Search on the array to calculate the 
        average case for a successful search.
        a) Calculates log_2(n + 1).
        b) Identifies the numbers that require the most comparisons.
        c) Computes the average number of comparisons.
        """
        print(f"a) log_2(n+1) = log_2({self.length} + 1) = "
            f"{self.largest_key()}\n")
        
        total_count = 0
        count_dict = {}
        
        print("Index\tNumber\tCount")
        for num in self.arr:
            count = self.binary_search_average(num)
            count_dict[num] = count
            mid = self.arr.index(num) + 1
            
            print(f"{mid:^5}\t{num:^5}\t{count:^5}")
            total_count += count 
            
        print(f"b) {self.largest_number_key(count_dict)}")
        
        avg = self.average(total_count, self.length)
        print(f"c) Average: {total_count} / {self.length} = {avg:.7f}")
        
    def largest_key(self):
        """ Calculates the largest key based on the array length. """
        return math.ceil(math.log2(self.length))
        
    def binary_search_average(self, num):
        """ Performs Binary Search for the average case on a 
        given number. """    
        low = 0
        high = len(self.arr) - 1
        count = 0
        
        while low <= high:
            mid = (low + high) // 2
            count += 1

            if num < self.arr[mid]:
                high = mid - 1
            elif num > self.arr[mid]:
                low = mid + 1
            else:
                break
        return count
            
    def largest_number_key(self, count_dict):
        """ Identifies the numbers that required the largest 
        number of comparisons during Binary Search. """
        list = []
        for key, value in count_dict.items():
            if value == self.largest_key():
                list.append(key)
        return list    

    def average(self, a, b):
        """ Calculates the average by dividing the total count 
        by the number of elements. """
        return a / b if b != 0 else a
    # End of the performing Binary Search with average-case

    # Performing Binary Search with worst-case
    def worst_binary_search(self):
        """ 
        Simulates Binary Search in the worst case by introducing 
        a new element into the array, which increases the length. 
        This helps analyze the worst-case performance.
        """
        def new_list(index : int, number : int) -> list:
            """ Generate a new list for new length """
            aux_nums = [num + 1 for num in self.arr]
            aux_nums.insert(index, number)
            return sorted(aux_nums)
        
        aux_nums = new_list(3, 2)
        
        print(f"\nThe new list of numbers: {aux_nums}")
        print(f"The new length of the array: {len(aux_nums)}")
        
        total_count = 0
        count_dict = {}
        
        print("Index\tNumber\tCount")
        for num in aux_nums:
            count = self.binary_search_worst(num)
            count_dict[num] = count
            mid = aux_nums.index(num) + 1
            
            print(f"{mid:^5}\t{num:^5}\t{count:^5}")
            total_count += count
        
        avg = self.average(total_count, len(aux_nums))
        print(f"c) Average: {total_count} / {len(aux_nums)} = {avg:.7f}")
    
    def binary_search_worst(self, num):    
        """ Performs Binary Search for the worst-case scenario on 
        a given number. """
        low = 0
        high = len(self.arr) - 1
        count = 0
        
        while low <= high:
            mid = (low + high) // 2
            count += 1

            if num < self.arr[mid]:
                high = mid - 1
            elif num > self.arr[mid]:
                low = mid + 1
            else:
                low = high + 1
        return count
    # End of the Performing Binary Search with worst-case
    
    def __str__(self):
        """ Returns a string representation of the array. """
        return str(self.arr)

class BinaryVsSequentialSearch:
    """  A class to compare the performance of Binary Search 
    (O(log n)) and Sequential Search (O(n)).
    
    Attributes:
        base (int): The base number used in the search.
        exponent (int): The exponent used to compute the size.
    """
    def __init__(self, base, exponent):
        self.setBase(base)
        self.setExponent(exponent)
    
    def setBase(self, base):
        """ Validates and sets the base number for search calculations. 
        If the base is less than or equal to 0, it defaults to 10."""
        base = int(base)
        self.base = base if base > 0 else 10
    
    def setExponent(self, exponent):
        """ Validates and sets the exponent for search calculations. 
        If the exponent is less than or equal to 0, it defaults to 5."""
        exponent = int(exponent)
        self.exponent = exponent if exponent > 0 else 5
        
    def getNumber(self):
        """ Computes the size of the search space using the 
        formula `base^(exponent)`. """
        return self.base ** (self.exponent)
                    
    def get_sequential_average(self):
        """ Returns the average number of comparisons 
        for Sequential Search (O(n). """
        return self.getNumber() / 2

    def get_binary_average(self):
        """ Returns the average number of comparisons for 
        Binary Search (O(log n)) by calculating the logarithm 
        of the base to the base 2."""
        return math.log(self.getNumber(), 2)

    def average(self):
        """ Computes and returns the ratio of the average number 
        of comparisons between Sequential and Binary Search. """
        linear = self.get_sequential_average()
        binary = self.get_binary_average()
        results = (linear / binary)
        return round(results / 1000) * 1000


def get_numbers_from_user():
    """
        Prompts the user to enter numbers separated by commas and 
        returns them as a list of non-negative integers.
    """

    user_input = input("Enter numbers separated by commas:")
    try:
        numbers = [int(num.strip()) for num in user_input.split(',')]
        if any(num < 0 for num in numbers):
            print(f"Invalid input: {numbers} (negative numbers are not allowed)")
            return []
        return numbers
    except ValueError:
        print("Invalid input! Please enter only numbers.")
        return []

def main():
    """ 
        Displays a menu for selecting searching algorithm analyses.

        Options:
            2. Analyze Binary Search (average-case scenario)
            3. Analyze Binary Search (worst-case scenario)
            4. Compare Binary Search vs Sequential Search
    """

    while True: 
        print("\nMenu of Searching Algorithms:")
        print("1. Return to the Main Menu")
        print("2. Analyze Binary Search with average-case scenario")
        print("3. Analyze Binary Search with worst-case scenario")
        print("4. Analyze Binary Search vs. Sequential Search")

        choice = input("Enter your choice: ")

        if choice == '1':
            return
        elif choice == '2':
            arr_num = []
            
            print("\nAverage-case scenario in successful search...")
            arr_num = get_numbers_from_user()
            
            search = ArraySearching(arr_num)
            print(f"\nThe array is: {search}")
            print(f"The length is: {search.length}\n")
            search.average_binary_search()

        elif choice == '3':
            arr_num = []
            
            print("\nWorst-case scenario in unsuccessful search...")
            arr_num = get_numbers_from_user()

            search = ArraySearching(arr_num)
            print(f"\nThe array is: {search}")
            print(f"The length of the array is: {search.length}")
            search.worst_binary_search()

        elif choice == '4':
            try:
                print("Sequential vs Binary Search...")                
                base = input("Enter the base: ")
                exponent = input("Enter the exponent: ")
                
                bs = BinaryVsSequentialSearch(base, exponent)
                
                print("\nEstimating how many times faster search...")
                time.sleep(2)
                print(f"Sequential: {bs.get_sequential_average()}")
                print(f"Binary:     {bs.get_binary_average():.6f}")
                print(f"Result:     {bs.average()}")
            except ValueError:
                print("Invalid input!")
        else:
            print("Invalid choice! Please enter a valid option.")
