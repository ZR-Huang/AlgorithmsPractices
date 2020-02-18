'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.

Example 1:
Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
'''
from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [None] * n
        dp[0] = True
        for i in range(1, n):
            for step in range(1, n):
                if nums[i-step] >= step and dp[i-step]:
                    dp[i] = True
                    break
                dp[i] = False
        return dp[-1]

    def canJump(self, nums: List[int]) -> bool:
        # greedy
        last = len(nums)-1
        for i in range(len(nums)-1, -1, -1):
            if nums[i] + i >= last:
                last = i
        
        return last == 0

print(Solution().canJump([2,3,1,1,4]))
print(Solution().canJump([3,2,1,0,4]))
print(Solution().canJump([0,1]))
