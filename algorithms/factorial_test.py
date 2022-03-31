from unittest import TestCase
from factorial import Factor
import math

class TestFactorial(TestCase):
    def test_valid_factorials (self):
        self.assertEqual (Factor.myfactorial(5), 120)
        self.assertEqual (Factor.myfactorial(4), 24)
        self.assertEqual (Factor.myfactorial(0), 1)
        self.assertEqual (Factor.myfactorial(1), 1)
 
    def test_negative_factor (self):
        self.assertTrue(math.isnan(Factor.myfactorial(-1)))