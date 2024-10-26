import unittest
from tax_calculator import calculate_tax

class TestTaxCalculator(unittest.TestCase):
    def test_no_tax(self):
        self.assertEqual(calculate_tax(10000), 0)

    def test_low_income_tax(self):
        self.assertEqual(calculate_tax(15000), 600)  # 20% of (15000 - 12000)

    def test_high_income_tax(self):
        self.assertEqual(calculate_tax(40000), 6400)  # 20% of (36000 - 12000) + 40% of (40000 - 36000)
