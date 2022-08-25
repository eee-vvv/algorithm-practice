import unittest
from how_sum import *

class TestDynamicProgrammingMethods(unittest.TestCase):
    def test_how_sum(self):
        nums = [500]
        targ = 321
        self.assertEqual(how_sum(targ, nums), None )

if __name__ == '__main__':
    unittest.main()