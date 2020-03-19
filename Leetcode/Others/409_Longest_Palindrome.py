'''
Given a string which consists of lowercase or uppercase letters, find the length of 
the longest palindromes that can be built with those letters.
This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:
Input:
"abccccdd"
Output:
7
Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
'''
class Solution:
    def longestPalindrome(self, s: str) -> int:
        '''
        the numbers of all letters occur in a palindrome are 
        even except the mid one for a palindrome with an odd length.
        So we can greedly add up numbers of different letters.
        '''
        if not s :
            return 0
        ans, hashmap, odd_exist = 0, {}, False
        for c in s:
            hashmap[c] = hashmap[c] + 1 if c in hashmap else 1
        for value in hashmap.values():
            if value & 1 == 0:
                ans = ans + value
            else:
                ans = ans + value - 1
                odd_exist = True
        return ans + int(odd_exist)