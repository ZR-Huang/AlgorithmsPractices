"""
Given two string s and t, write a function to determine 
if t is an anagram of s.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
"""

import unittest

class TestSolutionMethods(unittest.TestCase):
    def test_isAnagram(self):
        so = Solution()

        s = "anagram"
        t = "nagaram"
        self.assertEqual(so.isAnagram(s, t), True)

        s = "rat"
        t = "car"
        self.assertEqual(so.isAnagram(s, t), False)

        s = ""
        t = "car"
        self.assertEqual(so.isAnagram(s, t), False)

        s = "rat"
        t = ""
        self.assertEqual(so.isAnagram(s, t), False)

        s = ""
        t = ""
        self.assertEqual(so.isAnagram(s, t), True)

        s = "ab"
        t = "a"
        self.assertEqual(so.isAnagram(s, t), False)


class Solution:
    def isAnagram(self, s, t):
        """
        Time complexity: O(N), the length of s is donated as N.
        Space complexity: O(1), the maximum size of the table is 26.
        """
        
        if len(s) != len(t):
            return False
        else:
            d_of_s = {}
            for c in s:
                d_of_s[c] = d_of_s[c]+1 if c in d_of_s else 1
            
            for c in t:
                if not c in d_of_s or d_of_s[c] -1<0:
                    return False
                else:
                    d_of_s[c] -= 1
            return True

if __name__=='__main__':
    unittest.main()