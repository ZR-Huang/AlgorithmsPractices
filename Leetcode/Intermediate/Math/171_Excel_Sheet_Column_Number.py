'''
Given a column title as appear in an Excel sheet, return its corresponding column number

For example:
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...

Example 1:
Input: "A"
Output: 1

Example 2:
Input: "AB"
Output: 28

Example 3:
Input: "ZY"
Output: 701
'''

class Solution:
    def titleToNumber(self, s: str) -> int:
        base = ord('A') - 1
        reverse_s = s[::-1]
        ans = 0
        for i, value in enumerate(reverse_s):
            ans += (26**i) * (ord(value) - base)
        return ans