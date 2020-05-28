import unittest
from Calculator import Calculator

class MyTest (unittest.TestCase):
    def test_add(self):
        calcObject = Calculator(2,5)
        x = calcObject.add()
        self.assertEqual(7, x)

if __name__ == '__main__':
    unittest.main()