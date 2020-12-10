import unittest
from Factorial import fact

class TestFactorial(unittest.TestCase):
    def test_fact(self):
        self.assertEqual(fact(0),1)
        
unittest.main(argv=[''],verbosity=2,exit=False)