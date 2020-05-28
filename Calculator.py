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
