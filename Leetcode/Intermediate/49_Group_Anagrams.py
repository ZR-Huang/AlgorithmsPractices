"""
Given an array of strings, group anagrams together.

Example:
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Note:
- All inputs will be in lowercase.
- The order of your output does not matter.
"""

class Solution:
    def groupAnagrams(self, strs):
        def hash(d):
            l = []
            for k, v in sorted(d.items(), key=lambda item: item[0]):
                l.append(k + str(v))
            return ''.join(l)

        def count(s):
            d = {}
            for char in s:
                if char in d:
                    d[char] += 1
                else:
                    d[char] = 1
            return d
        
        ans = {}
        for s in strs:
            d = count(s)
            hash_value = hash(d)
            if hash_value in ans:
                ans[hash_value].append(s)
            else:
                ans[hash_value] = [s]
        
        return list(ans.values())

    def groupAnagrams_v2(self, strs):
        """
        Time : O(NKlogK), N is the number of strs, K is the maximum length of the string in strs.
        Space: O(NK)
        """
        import collections

        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        
        return list(ans.values())

    
    def groupAnagrams_v3(self, strs):
        """
        Time : O(NK)
        Space: O(NK)
        """
        import collections
        def hash(s):
            res = [0] * 26
            for char in s:
                res[ord(char) - ord('a')] += 1
            
            return tuple(res)

        ans = collections.defaultdict(list)
        for s in strs:
            ans[hash(s)].append(s)
        
        return list(ans.values())


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
        