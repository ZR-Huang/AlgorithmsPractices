"""
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
"""

import unittest


class TestSolutionMethods(unittest.TestCase):
    def test_myAtoi(self):
        so = Solution()

        s = "42"
        self.assertEqual(so.myAtoi(s), 42)

        s = "   -42"
        self.assertEqual(so.myAtoi(s), -42)

        s = "   +42"
        self.assertEqual(so.myAtoi(s), 42)

        s = "4193 with words"
        self.assertEqual(so.myAtoi(s), 4193)

        s = "words and 987"
        self.assertEqual(so.myAtoi(s), 0)

        s = "-91283472332"
        self.assertEqual(so.myAtoi(s), -2147483648)

        s = "91283472332"
        self.assertEqual(so.myAtoi(s), 2**31-1)
        
        s = "words and +sdfsd"
        self.assertEqual(so.myAtoi(s), 0)

        s = "3.14159"
        self.assertEqual(so.myAtoi(s), 3)

        s = ".1"
        self.assertEqual(so.myAtoi(s), 0)
        
        s = " "
        self.assertEqual(so.myAtoi(s), 0)


class Solution:
    def myAtoi(self, s):
        """
        Time complexity: O(N)
        Space complexity: O(1)
        """
        length = len(s)
        if length == 0:
            return 0
        
        # find the numerical substring.
        start = -1
        end = -1
        for index, c in enumerate(s):
            if c.isdigit() or c == '+' or c=='-':
                start = index
                end = index+1
                while end < length and s[end].isdigit():
                    end += 1
                end -= 1 # the last position of the end is not digit
                break
            elif c != ' ':
                return 0
            else:
                continue
        
        if start == -1:
            return 0
            
        # start conversion
        sign = 1
        if s[start] == '+':
            start += 1
        elif s[start] == '-':
            sign = -1
            start += 1
        
        ans = 0
        while start <= end:
            ans = ans*10 + (ord(s[start])-ord('0'))
            start += 1
        ans *= sign
        if ans > 2**31-1:
            ans = 2**31-1
        elif ans < -2**31:
            ans = -2**31
        return ans
    
    def myAtoi(self, str: str) -> int:
        curr, length, integer, sign = 0, len(str), 0, 1
        if length == 0:
            return 0
        # discard whitespace
        while curr < length:
            if str[curr] != ' ':
                break
            curr += 1
        if curr < length:
            if str[curr] == '-':
                sign = -1
                curr += 1
            elif str[curr] == '+':
                curr += 1
            
            while curr < length and str[curr].isdigit():
                integer *= 10
                integer += int(str[curr])
                curr += 1
        
        integer *= sign
        INT_MAX, INT_MIN = 2**31-1, -(2**31)
        if integer > INT_MAX:
            return INT_MAX
        elif integer < INT_MIN:
            return INT_MIN
        else:
            return integer
        

if __name__ == "__main__":
    unittest.main()