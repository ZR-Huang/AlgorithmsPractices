import unittest

class TestSolutionMethods(unittest.TestCase):

    def test_reverse(self):
        s = Solution()
        # test the example 1
        x = 123
        self.assertEqual(s.reverse(x), 321)

        # test the example 2
        x = -123
        self.assertEqual(s.reverse(x), -321)

        # test the example 3
        x = 120
        self.assertEqual(s.reverse(x), 21)

        # test the overflows of the reversed integers
        x = 1534236469
        self.assertEqual(s.reverse(x), 0)

        # test the special inputs
        x = 0
        self.assertEqual(s.reverse(x), 0)

        


class Solution:
    
    def reverse(self, x) -> int:
        def helper(x, sign):
            x *= sign
            result = x % 10
            x = x // 10
            while x != 0:
                result = result * 10 + x % 10
                x = x // 10
            
            result *= sign
            if result > 2**31-1 or result < -2**31:
                result = 0
            return result
        
        if x == 0:
            return 0
        elif x > 0:
            return helper(x, 1)
        else:
            return helper(x, -1)

    
            

if __name__ == '__main__':
    unittest.main()