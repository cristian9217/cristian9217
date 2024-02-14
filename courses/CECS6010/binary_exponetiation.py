class BinaryExponentiation: 
    def __init__(self, a = 2, n = 17):
        if a <= 0:
            raise ValueError("Base must be positive.")
        self.a = a

        if n <= 0:
            raise ValueError("Exponent must be positive.")
        self.n = n

    def left_right_binary_exponentiation(self):
        binary_n = bin(self.n)[self.a:] 

        print(f"n = {self.n} = ({binary_n})_2")

        for i, bit in enumerate(binary_n):
            if bit == '1':
                if(i == 0):
                    print(f"1 = a")
                else:
                    print(f"1 = a^{2 ** i} * a")
            else:
                print(f"0 = a^{2 ** i}")

    def right_left_binary_exponentiation(self):
        binary_n = bin(self.n)[self.a:] 

        print(f"n = {self.n} = ({binary_n})_2")
        binary_n = binary_n[::-1]

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
    while True: 
        print("\nMenu of Binary Exponetiation:")
        print("1. Return to the Main Menu")
        print("2. Apply left-to-rigth binary exponentation")
        print("3. Apply right-to-left binary exponentation")

        choice = input("Enter your choice: ")
        
        if choice == '1':
            return

        elif choice == '2':
            try:
                num = int(input("Enter the number n: "))

                binaryLeft = BinaryExponentiation(n = num)
                print(str(binaryLeft))
                binaryLeft.left_right_binary_exponentiation()
            
            except ValueError:
                print("Invalid input! Please enter numbers only.")
        
        elif choice == '3':
            try:
                num = int(input("Enter the number n: "))

                binaryRight = BinaryExponentiation(n = num)
                print(str(binaryRight))
                binaryRight.right_left_binary_exponentiation()
            
            except ValueError:
                print("Invalid input! Please enter numbers only.")
        
        else:
            print("Invalid choice! Please enter a valid option.")