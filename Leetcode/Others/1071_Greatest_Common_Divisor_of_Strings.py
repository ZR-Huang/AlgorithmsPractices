'''
For strings S and T, we say "T divides S" if and only if S = T + ... + T  
(T concatenated with itself 1 or more times)

Return the largest string X such that X divides str1 and X divides str2.

Example 1:
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Example 2:
Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Example 3:
Input: str1 = "LEET", str2 = "CODE"
Output: ""

Note:
- 1 <= str1.length <= 1000
- 1 <= str2.length <= 1000
- str1[i] and str2[i] are English uppercase letters.
'''
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # time: O(N+logN) N =len(str1)+len(str2)
        # space: O(N)
        len_str1, len_str2 = len(str1), len(str2)
        shorter, longer = min([len_str1, len_str2]), max([len_str1, len_str2])
        while shorter > 0:
            tmp1 = longer % shorter
            longer = shorter
            shorter = tmp1
        if str1[:longer]*(len_str1//longer) == str1 and str1[:longer]*(len_str2//longer)==str2:
            return str1[:longer]
        return ''

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # time: O(N+logN) N =len(str1)+len(str2)
        # space: O(N)
        # analysis: https://leetcode-cn.com/problems/greatest-common-divisor-of-strings/solution/zi-fu-chuan-de-zui-da-gong-yin-zi-by-leetcode-solu/
        if str1+str2 != str2+str1:
            return ''
        len_str1, len_str2 = len(str1), len(str2)
        shorter, longer = min([len_str1, len_str2]), max([len_str1, len_str2])
        while shorter > 0:
            tmp1 = longer % shorter
            longer = shorter
            shorter = tmp1
        return str1[:longer]

print(Solution().gcdOfStrings("ABCABC","ABC"))