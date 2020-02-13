'''
Given a collection of distinct integers, return all possible permutations.

Example:
Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def helper(nums, permutation):
            nonlocal ans
            if not nums:
                ans.append(permutation)
                return
            for i, value in enumerate(nums):
                helper(nums[:i]+nums[i+1:], permutation + [value])
                
        helper(nums, list())
        return ans

print(Solution().permute([1,2,3]))