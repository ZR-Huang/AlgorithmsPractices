'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''

class Solution:
    def generateParenthesis(self, n: int):
        if n == 0:
            return [""]
        ans = []
        def helper(string, left, right):
            nonlocal ans
            if right > left:
                return
            if len(string) == 2*n:
                ans.append(string)
                return
            for c in ["(", ")"]:
                if c == "(" and left + 1>n:
                    continue
                elif c == "(":
                    helper(string+c, left+1, right)
                elif c == ")" and right + 1>n:
                    continue
                elif c == ")":
                    helper(string+c, left, right+1)
                
        helper("", 0, 0)
        return ans

print(Solution().generateParenthesis(3))