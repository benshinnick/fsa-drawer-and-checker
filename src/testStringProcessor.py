import unittest

from .fsa import FiniteStateAutomata

class TestStringMethods(unittest.TestCase):

    # Must comment out fsa main code before running

    def test_valid_strings(self):
        fsa = FiniteStateAutomata("input-files/fsa.txt")
        self.assertTrue(fsa.check_string("xxxxxyxxxyxxxzxxxa"))
        self.assertTrue(fsa.check_string("xxxxxxxxxxy"))
        self.assertTrue(fsa.check_string("xxxxxyxxxxxxxxxxxy"))
        self.assertTrue(fsa.check_string("xxxxxyxxxyxxxxx"))
        self.assertTrue(fsa.check_string("xxxxxxxxxyxxxxxxxxyxxxxxxxzxxxxxxa"))
        self.assertTrue(fsa.check_string("xxxxxxxxxyxxxxxxxxyxxxxxxxzxxxxxxaxxxxxy"))
    
    def test_invalid_strings(self):
        fsa = FiniteStateAutomata("input-files/fsa.txt")
        self.assertFalse(fsa.check_string(""))
        self.assertFalse(fsa.check_string("xxxxxxxxx"))
        self.assertFalse(fsa.check_string("xxxxxyxxxxxxxxxxx"))
        self.assertFalse(fsa.check_string("xxxxxxxxxyxxxxxxxxyxxxxxxxz"))
        self.assertFalse(fsa.check_string("xxxxxxxxxyxxxxxxxxyxxxxxxxzxxxx"))

if __name__ == '__main__':
    unittest.main()