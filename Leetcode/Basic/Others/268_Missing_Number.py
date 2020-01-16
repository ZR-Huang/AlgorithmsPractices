'''
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:
Input: [3,0,1]
Output: 2

Example 2:
Input: [9,6,4,2,3,5,7,0,1]
Output: 8

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
'''

class Solution:
    def missingNumber(self, nums) -> int:
        if not nums:
            return 0
        # according to Gaussian sum formula
        sum_of_0_to_n = len(nums) * (len(nums)+1) // 2

        for n in nums:
            sum_of_0_to_n -= n
        
        return sum_of_0_to_n

print(Solution().missingNumber([3,0,1]))