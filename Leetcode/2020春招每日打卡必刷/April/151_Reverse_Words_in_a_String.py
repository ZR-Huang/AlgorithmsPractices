'''
Given an input string, reverse the string word by word.

Example 1:
Input: "the sky is blue"
Output: "blue is sky the"

Example 2:
Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:
Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

Note:
    A word is defined as a sequence of non-space characters.
    Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
    You need to reduce multiple spaces between two words to a single space in the reversed string.

Follow up:
For C programmers, try to solve it in-place in O(1) extra space.
'''
from collections import deque
class Solution:
    def reverseWords(self, s: str) -> str:
        # API
        s = s.strip()
        s = s.split(" ")
        s.reverse()
        return " ".join(filter(bool, s))

    def reverseWords(self, s: str) -> str:
        # 双向队列
        q, word = deque(), []
        left, right = 0, len(s)-1
        # strip
        while left <= right and s[left] == ' ':
            left += 1
        while left <= right and s[right] == ' ':
            right -= 1
        while left <= right:
            if s[left] == ' ' and word:
                q.appendleft(''.join(word))
                word = []
            elif s[left] != ' ':
                word.append(s[left])
            left += 1
        q.appendleft(''.join(word))
        return ' '.join(q)