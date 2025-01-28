"""
Module Name: sorting.py
Description: A Python module implementing sorting 
algorithms such as Insertion, Merge and Quick Sort.
Author: Cristian M. Pagan
Date: February 14, 2024
"""

class ArraySorting:
    """
        A class to perform various sorting algorithms on arrays.
    
        Attributes:
            arr (list): The array to be sorted.
    """
    def __init__(self, arr):        
        """ Initializes the object with the given array or string. """
        self.set_array(arr)
    
    def set_array(self, arr):
        """ Sets the array. """
        # If the array is empty, default list.
        # Else the array is not empty, convert to a list.
        if not arr:
          self.arr = ['E', 'X', 'A', 'M', 'P', 'L', 'E']
        elif isinstance(arr, str):
            self.arr = list(arr.upper()) 
        else:
            self.arr = list(arr)
            
    def get_array(self):
        """ Returns the current array. """
        return self.arr

    # Insertion Sort
    def insertion_sort(self):
        """ Sorts the array using the insertion sort algorithm. """
        for idx in range(1, len(self.arr)):
            pos = idx
            temp_elem = self.arr[idx]
            while pos > 0 and self.arr[pos - 1] > temp_elem:
                self.arr[pos] = self.arr[pos - 1]
                pos -= 1
            self.arr[pos] = temp_elem

            print(f"After iteration {idx}: {self}")
    # End of the Insertion Sort

    # Merge Sort
    def merge_sort(self):
        self.merge_sort_helper(self.arr)
        
    def merge_sort_helper(self, arr):
        """ Sorts the array using the merge sort algorithm. """
        if len(arr) > 1:
            mid = len(arr) // 2

            temp1 = arr[:mid]
            temp2 = arr[mid:]

            print(f"Left half: {temp1}")
            print(f"Right half: {temp2}")

            self.merge_sort_helper(temp1)   # sort first half
            self.merge_sort_helper(temp2)   # sort second half
            
            print(f"Merging: {temp1} and {temp2}")
            
            self.merge(temp1, temp2, self.arr)  # merge both halves

    def merge(self, temp1, temp2, arr):
        i = j = k = 0

        while i < len(temp1) and j < len(temp2):
            if temp1[i] < temp2[j]:
                arr[k] = temp1[i]
                i += 1
            else:
                arr[k] = temp2[j]
                j += 1
            k += 1

        while i < len(temp1):
            arr[k] = temp1[i]
            i += 1
            k += 1

        while j < len(temp2):
            arr[k] = temp2[j]
            j += 1
            k += 1
    # End of the Merge Sort

    # Quick Sort
    def quick_sort(self):
        """ Sorts the array using the merge sort algorithm. """
        self.quick_sort_helper(self.arr, 0, len(self.arr) - 1)

    def quick_sort_helper(self, arr, low, high):
        if low < high:
            print(f"{arr} (Before Partition)")
            pivotIdx = self.partition(arr, low, high)
            print(f"{arr} (Pivot: {arr[pivotIdx]})")
            self.quick_sort_helper(arr, low, pivotIdx - 1)
            self.quick_sort_helper(arr, pivotIdx + 1, high)
    
    def partition(self, arr, low, high):
        pivot = arr[low]
        left = low + 1
        right = high

        while left <= right:
            while left <= high and arr[left] <= pivot:
                left += 1
            while right >= low and arr[right] > pivot:
                right -= 1
            if left < right:
                arr[left], arr[right] = arr[right], arr[left]

        arr[low], arr[right] = arr[right], arr[low]
        return right
    # End of the Quick Sort
    
    def __str__(self):
        """ Returns the string representation of the array. """
        return str(self.arr)

def main():
    """ Provides a menu for selecting the sorting method. """
    while True: 
        # Displaying the menu options for the user
        print("\nMenu of Sorting Algorithms:")
        print("1. Return to the Main Menu")
        print("2. Sort a word using Insertion Sort")
        print("3. Sort a word using Merge Sort")
        print("4. Sort a word using Quick Sort")
        choice = input("Enter your choice: ")
        
        # Return to the Main Menu.
        if choice == '1':
            return
        # Sorting a word using Insertion Sort.
        elif choice == '2':
            input_word = input("Enter a word: ")
            sort = ArraySorting(input_word)
            print("Using Insertion Sort...")
            print(f"Original array: {sort}")
            sort.insertion_sort()
            print(f"Sorted array: {sort}")
        # Sorting a word using Merge Sort.
        elif choice == '3':
            input_word = input("Enter a word: ")
            sort = ArraySorting(input_word)
            print("Using Merge Sort...")
            print(f"Original array: {sort}")
            sort.merge_sort()
            print(f"Sorted array: {sort}")
        # Sorting a word using Quick Sort.
        elif choice == '4':
            input_word = input("Enter a word: ")
            sort = ArraySorting(input_word)
            print("Using Quick Sort...")
            print(f"Original array: {sort}")
            sort.quick_sort()
            print(f"Sorted array: {sort}")
        # When user do not select the right option.
        else:
            print("Invalid choice! Please enter a valid option.")
