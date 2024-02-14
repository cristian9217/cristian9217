class IntArraySorting:

    def __init__(self, arr):        
        if len(arr) == 0:
            self.arr = ['E', 'X', 'A', 'M', 'P', 'L', 'E']
        else:
            self.arr = [x.upper() if isinstance (x, str) 
                        else x for x in arr]

    def get_arr(self):
        return self.arr

    # Insertion Sort
    def insertion_sort(self):
        for idx in range(1, len(self.arr)):
            pos = idx
            temp_elem = self.arr[idx]
            while pos > 0 and self.arr[pos - 1] > temp_elem:
                self.arr[pos] = self.arr[pos - 1]
                pos -= 1
            self.arr[pos] = temp_elem

            print(f"After iteration {idx}: {self}")

    # Merge Sort
    def merge_sort(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2

            temp1 = arr[:mid]
            temp2 = arr[mid:]

            print(f"Left half: {temp1}")
            print(f"Right half: {temp2}")

            self.merge_sort(temp1)   # sort first half
            self.merge_sort(temp2)   # sort second half
            
            print(f"Merging: {temp1} and {temp2}")
            
            self.merge(temp1, temp2, arr)  # merge both halves

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
    # Merge Sort

    # Quick Sort
    def quick_sort(self, arr):
        self.quickSortHelper(arr, 0, len(arr) - 1)

    def quickSortHelper(self, arr, low, high):
        if low < high:
            print(f"{arr} (Before Partition)")
            pivotIdx = self.partition(arr, low, high)
            print(f"{arr} (Pivot: {arr[pivotIdx]})")
            self.quickSortHelper(arr, low, pivotIdx - 1)
            self.quickSortHelper(arr, pivotIdx + 1, high)
    
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

    def __str__(self):
        return f"{self.arr}"

def main():
    while True: 
        print("\nMenu of Sorting Algorithms:")
        print("1. Return to the Main Menu")
        print("2. Sort a word using Insertion Sort")
        print("3. Sort a word using Merge Sort")
        print("4. Sort a word using Quick Sort")

        choice = input("Enter your choice: ")
        
        if choice == '1':
            return

        elif choice == '2':
            input_word = input("Enter a word: ")
            sort = IntArraySorting(list(input_word))
            print("Using Insertion Sort...")
            print(f"Original array: {sort}")
            sort.insertion_sort()
            print(f"Sorted array: {sort}")

        elif choice == '3':
            input_word = input("Enter a word: ")
            sort = IntArraySorting(list(input_word))
            print("Using Merge Sort...")
            print(f"Original array: {sort}")
            sort.merge_sort(sort.get_arr())
            print(f"Sorted array: {sort}")

        elif choice == '4':
            input_word = input("Enter a word: ")
            sort = IntArraySorting(list(input_word))
            print("Using Quick Sort...")
            print(f"Original array: {sort}")
            sort.quick_sort(sort.get_arr())
            print(f"Sorted array: {sort}")
        
        else:
            print("Invalid choice! Please enter a valid option.")
        
















