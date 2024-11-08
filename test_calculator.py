import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(5,-5 ),0)


    # Add the following test methods to the TestCalculator class:

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(2, 1), 1)
        self.assertEqual(self.calc.subtract(-10, -1), -9)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 3),6)
        self.assertEqual(self.calc.multiply(-2,-3),6)    
        self.assertEqual(self.calc.multiply(0, 0),0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2),5)
        self.assertEqual(self.calc.divide(20, 2),10)


    def test_modulo(self):
        self.assertEqual(self.calc.modulo(10,2),0)
        self.assertEqual(self.calc.modulo(15,2),1)



if __name__ == '__main__':
    unittest.main()