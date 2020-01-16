'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
1.Open brackets must be closed by the same type of brackets.
2.Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.

Example 1:
Input: "()"
Output: true

Example 2:
Input: "()[]{}"
Output: true

Example 3:
Input: "(]"
Output: false

Example 4:
Input: "([)]"
Output: false

Example 5:
Input: "{[]}"
Output: true
'''

class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True

        stack = []
        d = {'(':')', '{':'}', '[':']'}
        for c in s:
            if c in d:
                stack.append(d[c])
            else:
                if not stack or stack.pop() != c:
                    return False
        if stack:
            return False
        
        return True


print(Solution().isValid("(]"))