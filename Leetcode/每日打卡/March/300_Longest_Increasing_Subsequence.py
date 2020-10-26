'''
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:
Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 

Note:
- There may be more than one LIS combination, it is only necessary for you to return the length.
- Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?
'''

from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        length = len(nums)
        dp = [0] * length
        def helper(index, dp):
            if dp[index] > 0:
                return dp[index]
            maximum = 0
            for i in range(index):
                if nums[i] < nums[index]:
                    maximum = max([maximum, helper(i, dp)])
            dp[index] = maximum + 1
            return dp[index]
        
        for i in range(length):
            helper(i, dp)
        return max(dp)

    def lengthOfLIS(self, nums: List[int]) -> int:
        # O(n^2)
        if not nums:
            return 0
        length = len(nums)
        dp = [0] * length
        ans = 0
        for i in range(length):
            maximum = 0
            for j in range(i):
                if nums[j] < nums[i] and dp[j] > maximum:
                    maximum = dp[j]
            dp[i] = maximum + 1
            if dp[i] > ans:
                ans = dp[i]
        return ans

    def lengthOfLIS(self, nums: List[int]) -> int:
        # O(nlogn)
        # Solution Analysis: https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/zui-chang-shang-sheng-zi-xu-lie-dong-tai-gui-hua-2/
        if not nums:
            return 0
        tails, ans = [0] * len(nums), 0
        for num in nums:
            i, j = 0, ans
            while i < j:
                mid = (i + j) // 2
                if tails[mid] < num:
                    i = mid + 1
                else:
                    j = mid
            tails[i] = num
            if j == ans:
                ans += 1
        return ans

print(Solution().lengthOfLIS([4,10,4,3,8,9]))               
print(Solution().lengthOfLIS([10,9,2,5,3,7,101,18]))