"""
Module Name: horspool.py
Description: A Python module implementing the
Horspool algorithm for pattern matching in text.
Author: Cristian M. Pagan
Date: February 14, 2024
"""

class HorspoolString: 
    """
    A class to implement the Horspool algorithm for pattern 
    searching in strings.
    
    Attributes:
        text (str): The text to search for the pattern.
        pattern (str): The pattern to search in the text.
    """
    def __init__(self, text, pattern):
        """ Initializes the HorspoolString with text and pattern. """
        self.setText(text)
        self.setPattern(pattern)

    def setText(self, text):
        """ Sets the text attribute to the provided string. """        
        if not text.strip():
            self.text = "JIM_SAW_ME_IN_A_BARBERSHOP"
        else: 
            self.text = text.strip().upper()
            
    def setPattern(self, pattern):
        """ Sets the pattern to be searched. """        
        if not pattern.strip():
            self.pattern = "BARBER"
        else: 
            self.pattern = pattern.strip().upper()
    
    def get_shift_table(self):
        """Generates and prints a shift table. """
        
        # Count occurrences of each letter in the pattern
        letter_counts = {}
        for letter in self.pattern:
            letter_counts[letter] = letter_counts.get(letter, 0) + 1

        # Print the shift table
        print("Letter | Count")
        print("--------------")
        for letter, count in letter_counts.items():
            print(f"{letter:^6} | {count:^5}")
            
        # Wildcard (*) for unmatched characters
        print(f"{'*':^6} | {len(self.pattern):^5}")
    
    def get_horspool(self):
        def preprocess(pattern):
            table = {}
            for i in range(len(pattern) - 1):
                table[pattern[i]] = len(pattern) - 1 - i
            return table

        table = preprocess(self.pattern)
        n = len(self.text)
        m = len(self.pattern)
        i = m - 1  
        while i < n:
            k = 0
            while k < m and self.pattern[m - 1 - k] == self.text[i - k]:
                k += 1
            if k == m:
                return i - m + 1  
            else:
                skip = table.get(self.text[i], m)
                i += skip
        return -1  
        
    def display_match(self, matches):
        """ Displays the result of a matched pattern in the text. """
        
        # Calculate the end index of the match
        max_index = (matches + len(self.pattern)) - 1
        
        # Display table
        print(f"\n{'Pos':^6} | Letter | Letter")
        print("-------------------------")

        # Iterate through the text and display each character
        for i, word in enumerate(self.text):
            if matches <= i <= max_index:
                print(f"{i:^6} | {word:^6} | {self.text[i]:^6}")

    def __str__(self):
        return f"Text: {self.text}\nPattern: {self.pattern}"

class HorspolInteger:
    """
    A class to implement the Horspool algorithm for pattern 
    searching in strings.

    Attributes:
        text (str): The text to search for the pattern.
        length (int): The length of the text.
        pattern (str): The pattern to search in the text.
    """
    def __init__(self, text, length, pattern):
        """ Initializes the HorspoolString with text, length and pattern. """
        self.setLength(length)
        self.setText(text)
        self.setPattern(pattern)
    
    def setLength(self, length):
        """ Sets the length of the text. """
        try:
            # Try to convert the length to an integer
            length = int(length) 
            self.length = 1000 if length < 0 else length
        except ValueError:
            self.length = 1000

    def setText(self, text):
        """ Sets the text attribute to the provided string. """        
        if not text:
            self.text = "0" * self.length
        else: 
            self.text = f"{text}" * self.length
    
    def setPattern(self, pattern):
        """ Sets the pattern to be searched. """        
        if not pattern.strip():
            self.pattern = "00001"
        else: 
            self.pattern = pattern.strip()

    def compute_pattern(self):
        """ Computes and returns the new_len, position, 
        and result based on pattern matching. """

        # Reverse the pattern
        inverted_pattern = self.pattern[::-1]
        
        # Find the first occurrence of '1' in the inverted pattern
        position = None
        for i, num in enumerate(inverted_pattern):
            if num == '1':
                position = i + 1
                break
        if position is None:
            position = 0
        
        # Count the number of '1's in the pattern
        count_ones = self.pattern.count('1')
        
        # Calculate new_len based on the text and pattern length
        new_len = (len(self.text) - len(self.pattern) + 1) // count_ones 
        
        # Calculate the result as the product of new_len and position
        result = new_len * position
        
        return new_len, position, result

    def __str__(self):
        return f"\nLength: {self.length}\nPattern: {self.pattern}"

def main():
    while True: 
        print("\nMenu of Horspool's algorithm:")
        print("1. Return to the Main Menu")
        print("2. To search words")
        print("3. To search integers")
        choice = input("Enter your choice: ")
        
        # Return to the Main Menu.
        if choice == '1':
            return
        # Hoorspol's algorithm to search words.
        elif choice == '2':
            text = input("Enter the word: ")
            pattern = input("Enter the pattern: ")
            
            horspool = HorspoolString(text, pattern)
            
            print("The input entered: ")
            print(horspool)            
            
            horspool.get_shift_table()
            
            # Search for the pattern
            matches = horspool.get_horspool()
            
            if matches != -1:
                horspool.display_match(matches)    
            else:
                print("\nPattern not found.")
        # Hoorspol's algorithm to search integers.
        elif choice == '3':
            text = input("Enter the binary text: ")
            length = input("Enter the length: ")
            pattern = input("Enter the pattern: ")
            
            horspool = HorspolInteger(text, length, pattern)
            new_len, position, result = horspool.compute_pattern()
            
            print(f"The pattern '{horspool.pattern}' will be " + 
                  f"C = {new_len} * {position} = {result}")
        # When user do not select the right option.
        else:
            print("Invalid choice! Please enter a valid option.") 
