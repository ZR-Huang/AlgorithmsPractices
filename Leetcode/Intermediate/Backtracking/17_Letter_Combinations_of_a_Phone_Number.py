'''
Given a string containing digits from 2-9 inclusive, 
return all possible letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below. 
Note that 1 does not map to any letters.

Example:
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Note:
Although the above answer is in lexicographical order, 
your answer could be in any order you want.
'''

class Solution:
    def letterCombinations(self, digits: str):
        if not digits:
            return []
        digit2char = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno',
        '7':'pqrs', '8':'tuv', '9':'wxyz'}
        ans = []
        def helper(digits, digit2char, curr_i, length, string):
            nonlocal ans
            if curr_i >= length:
                ans.append(string)
                return
            for c in digit2char[digits[curr_i]]:
                helper(digits, digit2char, curr_i+1, length, string+c)
        
        helper(digits, digit2char, 0, len(digits), '')
        return ans

print(Solution().letterCombinations('23'))