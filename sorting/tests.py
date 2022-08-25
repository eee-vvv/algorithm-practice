from quick_sort import *
from bucket_sort import *
from radix_sort import *
import unittest

class TestSortingMethods(unittest.TestCase):
    def test_quick_sort(self):
        arr = [5,3,7,0,0]
        self.assertEqual(quick_sort(arr), [0,0,3,5,7])
        self.assertEqual(quick_sort(arr), sorted(arr))
        self.assertEqual(quick_sort(arr), arr) #quicksort modifies the array
        
    def test_bucket_sort(self):
        arrs = [[5,3,7,0,0], [1,2,3,4,5], [0,0,0,0,0,-1], [9,8,7,6,5,4,3,2,1,0]]
        for arr in arrs:
            self.assertEqual(bucket_sort(arr), sorted(arr))
            
    def test_order_mag(self):
        num_orders = [(0,0), (2,0), (10,1), (99,1), (100,2)]
        for num,order in num_orders:
            self.assertEqual(order_mag(num), order)
    
    def test_radix_sort(self):
        arrs = [[5,3,7,0,0], [1,2,3,4,5], [1,0,0,0,0,0], [9,8,7,6,5,5,4,3,2,8,1,0], [143,555,20,1,5432,554]]
        for arr in arrs:
            self.assertEqual(radix_sort(arr), sorted(arr))
        ## binary test
        arrs = [[111,10,0,1,11,10,100], [11110,1000000,100101011,0,11,10,101,100,1000,111], [1,0,0,0,0,0]]
        for arr in arrs:
            self.assertEqual(radix_sort(arr,2), sorted(arr))
        ## base 7 test
        arrs = [[1613,14,5,1,21,34,450], [66666,5435,6326,6424,0,6]]
        for arr in arrs:
            self.assertEqual(radix_sort(arr,7), sorted(arr))
        
if __name__ == '__main__':
    unittest.main()