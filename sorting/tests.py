from quick_sort import *
import unittest

class TestSortingMethods(unittest.TestCase):
    def test_quick_sort(self):
        arr = [5,3,7,0,0]
        self.assertEqual(quick_sort(arr), [0,0,3,5,7])
        self.assertEqual(quick_sort(arr), sorted(arr))
        self.assertEqual(quick_sort(arr), arr) #quicksort modifies the array
        
if __name__ == '__main__':
    unittest.main()