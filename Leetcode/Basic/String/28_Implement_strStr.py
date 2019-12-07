'''
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1

Clarification:
What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
'''

import unittest

class TestSolution(unittest.TestCase):
    def test_strStr(self):
        s = Solution()

        haystack = "hello"
        needle = "ll"
        self.assertEqual(s.strStr(haystack, needle), 2)

        haystack = "aaaaa"
        needle = "bba"
        self.assertEqual(s.strStr(haystack, needle), -1)

        haystack = "hello"
        needle = ""
        self.assertEqual(s.strStr(haystack, needle), 0)

        haystack = "aaa"
        needle = "aaaa"
        self.assertEqual(s.strStr(haystack, needle), -1)

        haystack = "mississippi"
        needle = "issip"
        self.assertEqual(s.strStr(haystack, needle), 4)

        haystack = "mississippi"
        needle = "issipi"
        self.assertEqual(s.strStr(haystack, needle), -1)

        haystack = "a"
        needle = "a"
        self.assertEqual(s.strStr(haystack, needle), 0)

    def test_strStr_v2(self):
        s = Solution()

        haystack = "hello"
        needle = "ll"
        self.assertEqual(s.strStr_v2(haystack, needle), 2)

        haystack = "aaaaa"
        needle = "bba"
        self.assertEqual(s.strStr_v2(haystack, needle), -1)

        haystack = "hello"
        needle = ""
        self.assertEqual(s.strStr_v2(haystack, needle), 0)

        haystack = "aaa"
        needle = "aaaa"
        self.assertEqual(s.strStr_v2(haystack, needle), -1)

        haystack = "mississippi"
        needle = "issip"
        self.assertEqual(s.strStr_v2(haystack, needle), 4)

        haystack = "mississippi"
        needle = "issipi"
        self.assertEqual(s.strStr_v2(haystack, needle), -1)

        haystack = "a"
        needle = "a"
        self.assertEqual(s.strStr_v2(haystack, needle), 0)





class Solution:
    def strStr(self, haystack, needle):
        '''
        Time Complexity : O(N**2) cannot pass the tests
        Space Complexity : O(1)
        '''
        len_h = len(haystack)
        len_n = len(needle)
        if not needle:
            return 0
        if len_n > len_h:
            return -1

        i = 0
        while i<len_h :
            found = True
            if haystack[i] == needle[0]:
                for j in range(len_n):
                    if i+j >= len_h or haystack[i+j] != needle[j]:
                        found = False
                        break
                if found:
                    return i

            i += 1
        
        return -1


    def strStr_v2(self, haystack, needle):
        '''
        Time Complexity : O(N**2) cannot pass the tests
        Space Complexity : O(1)
        '''
        len_h = len(haystack)
        len_n = len(needle)
        if not needle:
            return 0
        if len_n > len_h:
            return -1

        i = 0
        while i<len_h :
            found = True
            if haystack[i] == needle[0]:
                if haystack[i:i+len_n] == needle:
                    return i
                
            i += 1
        
        return -1


if __name__ == "__main__":
    unittest.main()