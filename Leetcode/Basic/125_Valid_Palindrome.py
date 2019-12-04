"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:
Input: "A man, a plan, a canal: Panama"
Output: true

Example 2:
Input: "race a car"
Output: false
"""

import unittest
class TestSolutionMethods(unittest.TestCase):
    def test_isPalindrome(self):
        so = Solution()

        s = "A man, a plan, a canal: Panama"
        self.assertEqual(so.isPalindrome(s), True)

        s = "race a car"
        self.assertEqual(so.isPalindrome(s), False)

        s = ""
        self.assertEqual(so.isPalindrome(s), True)

        s = ".,"
        self.assertEqual(so.isPalindrome(s), True)

        s = "0P"
        self.assertEqual(so.isPalindrome(s), False)


class Solution:
    def isPalindrome(self, s):
        """
        Time complexity: O(N)
        Space complexity: O(1)
        """
        if not s:
            return True
        
        i, j = 0, len(s)-1
        while i < j:
            while not s[i].isalnum() and i < j:
                i += 1
            while not s[j].isalnum() and i < j:
                j -= 1
            
            if s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else:
                return False
        return True


if __name__ == "__main__":
    unittest.main()