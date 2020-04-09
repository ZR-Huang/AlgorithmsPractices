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
from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = set()
        self.backtrack(0, 0, n, '', ans)
        return list(ans)
    
    def backtrack(self, left, right, n, prefix, ans):
        if len(prefix) == 2 * n:
            ans.add(prefix)
            return
        if left < n:
            self.backtrack(left+1, right, n, prefix+'(', ans)
        if right < left:
            self.backtrack(left, right+1, n, prefix+')', ans)

    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        stack = []
        stack.append(('', 0, 0)) # (prefix, left, right)
        while stack:
            prefix, left, right = stack.pop()
            if len(prefix) == 2 * n:
                ans.append(prefix)
            if left < n:
                stack.append((prefix+'(', left+1, right))
            if right < left:
                stack.append((prefix+')', left, right+1))
        return ans

print(Solution().generateParenthesis(3))