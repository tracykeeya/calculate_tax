import unittest
from tax_calculator import calculate_tax

class TestTaxCalculator(unittest.TestCase):
    def test_no_tax(self):
        self.assertEqual(calculate_tax(10000), 0)

if __name__ == '__main__':
    unittest.main()
