import math
import time

class IntArraySearching:

    def __init__(self, arr):        
        if len(arr) == 0:
            self.arr = [3, 14, 27, 31, 39, 42, 55, 
                        70, 74, 81, 85, 93, 98]
            self.length = 13
        else:
            self.arr = sorted([x for x in arr if x >= 0])
            self.length = len(arr)

    def largest_key(self):
        return math.ceil(math.log2(self.length))

    def largest_number_key(self, count_dict):
        list = [key for key, value in count_dict.items() if value == self.largest_key()]
        return f"{list}"

    # Binary Search
    def binary_search(self):
        
        print("a) Largest key comparisons? " + str(self.largest_key()))

        total_count = 0
        count_dict = {}
        print("Index\tNumber\tCount")

        for num in self.arr: 
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
            
            count_dict[num] = count
            
            print(f"{mid+1:^5}\t{num:^5}\t{count:^5}")
            total_count += count

        print("b) " + self.largest_number_key(count_dict))
        avg_binary = average_search(total_count, self.length)
        print(f"c) The average number of binary search: ")
        print(f"{total_count} / {self.length} = {avg_binary:.7f}")

    # Worst Case Binary Search
    def binary_search_worst_case(self):
        def new_list(index : int, number : int) -> list:
            """ Generate a new list for new length """
            aux_nums = [num + 1 for num in self.arr]
            aux_nums.insert(index, number)
            return sorted(aux_nums)
        
        aux_nums = new_list(index = 3, number = 2)   

        print(f"The new list of numbers: {aux_nums}")
        print(f"The new length of the array: {len(aux_nums)}\n")

        total_count = 0
        count_dict = {}
        print("Index\tNumber\tCount")
        
        for new_num in aux_nums:
            low = 0
            high = len(self.arr) - 1
            count = 0

            while low <= high:
                mid = (low + high) // 2
                count += 1

                if new_num < self.arr[mid]:
                    high = mid - 1
                elif new_num > self.arr[mid]:
                    low = mid + 1
                else:
                    low = high + 1

            count_dict[new_num] = count

            print(f"{mid+1:^5}\t{new_num:^5}\t{count:^5}")
            total_count += count

        avg_binary = average_search(total_count, len(aux_nums))
        print(f"c) The average number of binary search: ")
        print(f"{total_count} / {len(aux_nums)} = {avg_binary:.7f}")
    
    def __str__(self):
        return str(self.arr)

def average_search(a, b):
    return a / b



def main():
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
            
            print("Performing Binary Search with average-case scenario ")
            print("in successful search...")

            while True:
                user_input = input("Enter a number (type 'exit' to stop): ")
                if user_input.lower() == 'exit':
                    break
                try:
                    num = int(user_input)
                    if num < 0:
                        print(f"Invalid number: {num}")
                    arr_num.append(num)
                except ValueError:
                    print("Invalid input! Please enter only numbers.")
            
            searchAvg = IntArraySearching(arr_num)
            print(f"The array is: {searchAvg}")
            print(f"The length of the array is: {searchAvg.length}")
            searchAvg.binary_search()            

        elif choice == '3':
            arr_num = []
            
            print("Performing Binary Search with worst-case scenario ")
            print("in unsuccessful search...")
           
            while True:
                user_input = input("Enter a number (type 'exit' to stop): ")
                if user_input.lower() == 'exit':
                    break
                try:
                    num = int(user_input)
                    if num < 0:
                        print(f"Invalid number: {num}")
                    arr_num.append(num)
                except ValueError:
                    print("Invalid input! Please enter only numbers.")

            searchAvg = IntArraySearching(arr_num)
            print(f"The array is: {searchAvg}")
            print(f"The length of the array is: {searchAvg.length}")
            searchAvg.binary_search_worst_case()

        elif choice == '4':
            try:
                print("Note: Binary Search (O log n) and Sequential Search (O(n))")
                num = float(input("Enter the number: "))

                if num <= 1:
                    print(f"Invalid input: {num:.0f}! Please enter only positive numbers.")
                else:
                    result = num // math.ceil(math.log2(num))
                    print("Estimating how many times faster search...")
                    time.sleep(2)
                    print(f"{num:,.0f} / {math.ceil(math.log2(num))} = {result:,.0f} (aprox.)")
            
            except ValueError:
                print("Invalid input! Please enter numbers only.")
        else:
            print("Invalid choice! Please enter a valid option.")