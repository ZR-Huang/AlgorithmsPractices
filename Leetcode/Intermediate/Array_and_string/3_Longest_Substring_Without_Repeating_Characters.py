'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        A straight forward solution costing O(n^2) time
        Failed: Exceed time limitation.
        '''
        if not s:
            return 0
        
        length = len(s)
        if length == 1:
            return 1

        ans = 0
        for i in range(length):
            for j in range(i+1, length+1):
                substring = s[i:j]
                sub_len = len(substring)
                if len(set(substring)) == sub_len:
                    ans = max([ans, sub_len])

        return ans


    def lengthOfLongestSubstring_v2(self, s: str) -> int:
        '''
        Leverage binary-search to reduce the number of iterations.
        Time: O(nlogn)
        Failed: Exceed time limitation.
        '''
        def check(mid):
            for i in range(length-mid+1):
                substr = s[i:i+mid]
                sublen = len(substr)
                if sublen == len(set(substr)):
                    return True
            return False
            
        if not s:
            return 0
        
        length = len(s)
        if length == 1:
            return 1

        ans = 0
        l, r = 1, length
        while l <= r:
            mid = (l + r) >> 1
            if check(mid):
                ans = max([ans, mid])
                l = mid + 1
            else:
                r = mid - 1

        return ans

    def lengthOfLongestSubstring_v3(self, s: str) -> int:
        """
        Use the sliding window and hashset.
        Time : O(2n)
        """
        if not s:
            return 0
        
        curr_substr_set = set()
        l = 0
        ans = 0
        curr_len = 0
        for i in range(len(s)):
            curr_len += 1
            while s[i] in curr_substr_set:
                curr_substr_set.remove(s[l])
                l += 1
                curr_len -= 1
            if curr_len > ans:
                ans = curr_len
            curr_substr_set.add(s[i])
        return ans

    def lengthOfLongestSubstring_v4(self, s: str) -> int:
        """
        Use the sliding windows and hashmap
        Time : O(n)
        """
        l = 0
        curr_substr_map = {}
        ans = 0
        for i in range(len(s)):
            if s[i] in curr_substr_map:
                l = max([curr_substr_map[s[i]], l])
            ans = max([ans, i + 1 - l])     # +1 ensures the ans is right for the first letter.
            curr_substr_map[s[i]] = i + 1   # notice special indexes start from 1
        return ans
            

print(Solution().lengthOfLongestSubstring_v2("abababab"))