#Create a basic calculator GUI
import math

class Calculator:
#Value1 will be first instance, value2 will be second
#Assume value1 and value2 are entered as ints
    def __init__ (self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def add (self):
        return self.value1 + self.value2

    def subtract (self):
        return self.value1 - self.value2

    def multiply (self):
        return self.value1*self.value2

    def divide (self):
        return ((self.value1/self.value2) + (self.value1%self.value2))

    def Exponentiate (self):
        return math.pow(self.value1, self.value2)
    
    def log10 (self):
        return math.log10(self.value1)

def main():
    while (True):
        option = input("Enter the operation you would like to do\n1. Add \n2. Subtract \n3. Multiply \n4. Divide \n5. Exponentiate \n6. log10\n")
        value1 = input("Enter the first value\n")
        if option != "6":
            value2 = input("Enter the second value\n")

        option = int(option)
        value1 = int(value1)
        value2 = int(value2)

        obj = Calculator(value1, value2)

        if option == 1:
            print(obj.add())
        elif option == 2:
            print(obj.subtract())
        elif option == 3:
            print(obj.multiply())
        elif option == 4:
            print(obj.divide())
        elif option ==5:
            print(obj.Exponentiate())
        else:
            print(obj.log10())

        choice = input("Run again? (Y/N)\n")

        if choice == "N":
            break

main()