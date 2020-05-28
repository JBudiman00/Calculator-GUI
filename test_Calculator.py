import unittest
import Calculator

class MyTest (unittest.TestCase):
    def test_add(self):
        calcObject = Calculator(2,5)
        x = calcObject.add()
        self.assertNotEqual(7, x)

unittest.main