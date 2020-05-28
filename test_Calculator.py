import unittest
from Calculator import Calculator

class MyTest (unittest.TestCase):
    def test_add(self):
        calcObject = Calculator(5,5)
        x = calcObject.add()
        self.assertEqual(10, x)

    def test_subtract(self):
        calcObject = Calculator(5,5)
        a = calcObject.subtract()
        self.assertEqual(0, a)
    def test_multiply(self):
        calcObject = Calculator(5,5)
        b = calcObject.multiply()
        self.assertEqual(25, b)
    def test_divide(self):
        calcObject = Calculator(5,5)
        c = calcObject.divide()
        self.assertEqual(1, c)

if __name__ == '__main__':
    unittest.main()