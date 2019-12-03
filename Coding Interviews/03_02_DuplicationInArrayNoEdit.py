"""
The length of the array is n+1, and all the numbers range
from 1 to n, so there is one number is duplicated at least.
Find any of the duplications without modifying the array. 
"""

import unittest

class TestSolutionMethods(unittest.TestCase):
    def test_get_duplication(self):
        s = Solution()
        array = []
        self.assertEqual(s.get_duplication(array), -1)

        array = [1,4,2]
        self.assertEqual(s.get_duplication(array), -1)

        array = [2,3,5,4,3,2,6,7]
        self.assertIn(s.get_duplication(array), [2, 3])


class Solution:
    """
    There are two solutions. First, we can create a helper array 
    or a hashmap to solve this problem.
    Second, we compute the mid = (1+n) // 2. If the count of the numbers 
    which are in the [1, m] is more than m, and this interval does have 
    the duplications. Otherwise, the other interval does. 
    This solution is similar to the binary searching.
    """
    def get_duplication(self, numbers):
        length = len(numbers)
        if length < 1:
            return -1
        
        for num in numbers:
            if num > length-1 or num < 1:
                return -1

        start = 1
        end = length -1
        while end >= start:
            mid = (end + start) >> 1
            count = self.count_range(numbers, start, mid)
            if end == start:
                if count > 1:
                    return start
                else:
                    break
            if count > mid - start + 1:
                end = mid
            else:
                start = mid + 1
        return -1

    
    def count_range(self, numbers, l, r):
        count = 0
        for num in numbers:
            if num >= l and num <= r:
                count += 1
        return count


if __name__ == "__main__":
    unittest.main()