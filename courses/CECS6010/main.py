from math import log
import sorting
import binary_exponetiation as bin
import searching
import math

# Find the order of growth for solutions of recurrences.
def recurrences(a, b, d):
    if a > b**d:
        return f"a > b^d, O(n^log({a}, {b})) = O(n^{round(log(a, b))})" 
    elif a == b**d:
        return f"a = b^d, O(n^{d} log n)"
    else:
        return f"a = b^d, O(n^{d})"

def get_shift_table(pattern):
    letter_counts = {}

    for letter in pattern:
        letter_counts[letter] = letter_counts.get(letter, 0) + 1

    print("Letter | Count")
    print("--------------")
    for letter, count in letter_counts.items():
        print(f"{letter:^6} | {count:^5}")
    print(f"{'*':^6} | {len(pattern):^5}")

def horspool(text, pattern):
    def preprocess(pattern):
        table = {}
        for i in range(len(pattern) - 1):
            table[pattern[i]] = len(pattern) - 1 - i
        return table

    table = preprocess(pattern)
    n = len(text)
    m = len(pattern)
    i = m - 1  
    while i < n:
        k = 0
        while k < m and pattern[m - 1 - k] == text[i - k]:
            k += 1
        if k == m:
            return i - m + 1  
        else:
            skip = table.get(text[i], m)
            i += skip
    return -1  

def main():
    while True:
        print("\nMenu:")
        print("1. Analyze Sorting Algorithms")
        print("2. Analyze Searching Algorithms")
        print("3. Determine order of growth for a given recurrence")
        print("4. Apply binary exponentation")
        print("5. Apply Horspool's algorithm to search words")
        print("6. Apply Horspool's algorithm to search integers")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            sorting.main()

        elif choice == '2':
            searching.main()

        elif choice == '3':
            try:
                a = int(input("Enter the number a: "))
                b = int(input("Enter the number b: "))
                d = int(input("Enter the number d: "))

                if a < 1:
                    print(f"Invalid number: a = {a}!")
                elif b < 1:
                    print(f"Invalid number: b = {b}!")
                elif d < 1:
                    print(f"Invalid number: d = {d}!")
                else:
                    print(f"a = {a}, b = {b} and d = {d}.")
                    print(f"Since {recurrences(a, b, d)}")

            except ValueError:
                print("Invalid input! Please enter integers only.")

        elif choice == '4':
            bin.main()

        elif choice == '5':

            text = input("Enter the word: ").upper()
            pattern = input("Enter the pattern: ").upper()

            if len(text) == 0:
                text = "JIM_SAW_ME_IN_A_BARBERSHOP"
            if len(pattern) == 0:
                pattern = "BARBER"
            
            get_shift_table(pattern)

            # Search for the pattern
            matches = horspool(text, pattern)

            if matches != -1:
                max = (matches + len(pattern)) - 1
                print(f"\n{'Pos':^6} | Letter | Letter")
                print("-------------------------")
                for i, word in enumerate(text):
                    if matches <= i <= max:
                        print(f"{i:^6} | {word:^6} | {text[i]:^6}")
            else:
                print("\nPattern not found.")
       
        elif choice == '6':

            try:
                text = int(input("Enter the binary text: "))
                pattern = input("Enter the pattern: ")

                if not text:
                    text = "0"
                text = f"{text}" * 1000
                
                if len(pattern) == 0:
                    text = "00001"

                inverted_pattern = pattern[::-1]
                position = min([i+1 for i, num in enumerate(inverted_pattern) if num == '1'])
                count_ones = pattern.count('1')
                new_len = (len(text) - len(pattern) + 1) // count_ones 
                result = new_len * position

                print(f"The pattern '{pattern}' will be C = {new_len} " +
                    f"* {position} = {result}")
            
            except ValueError:
                print("Invalid input!")

        elif choice == '7':
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice! Please enter a valid option.")

if __name__ == "__main__":
    main()