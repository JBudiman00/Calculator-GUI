import unittest
from Calculator import Calculator

class MyTest (unittest.TestCase):
    def test_exponentiate(self):
        calcObject = Calculator(2,3)
        x = calcObject.Exponentiate()
        self.assertEqual(8, x)

    def test_log10(self):
        calcObject = Calculator(10, 10)
        a = calcObject.log10()
        self.assertEqual(1, a)
    
if __name__ == '__main__':
    unittest.main()