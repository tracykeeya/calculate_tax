import unittest
from factorial import factorial  # Import from factorial.py

class TestFactorial(unittest.TestCase):
    def test_factorial_of_0(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_of_1(self):
        self.assertEqual(factorial(1), 1)

    def test_factorial_of_5(self):
        self.assertEqual(factorial(5), 120)

    def test_factorial_of_6(self):
        self.assertEqual(factorial(6), 720)

if __name__ == '__main__':
    unittest.main()