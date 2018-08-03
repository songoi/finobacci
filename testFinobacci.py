import unittest
from finobacci import finobacciGen

class tests_finobacci(unittest.TestCase):
    def tests_finobacciGen(self):
        self.assertEqual(finobacciGen(1), [0,1,1])
        self.assertEqual(finobacciGen(2), [0,1,1,2])
        self.assertEqual(finobacciGen(4), [0,1,1,2,3,5])

if __name__ =='__main__':
    unittest.main()