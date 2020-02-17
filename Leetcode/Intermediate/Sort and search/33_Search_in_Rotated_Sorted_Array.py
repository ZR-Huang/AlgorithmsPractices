'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
'''
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        n = len(nums)
        if n == 1:
            return 0 if nums[0]==target else -1
        # Find pivot (Find the maximum in the array)
        index = self.find_maximum(nums)
        if target < nums[0]:
            right_ans = self.binary_search(nums, index+1, len(nums)-1, target)
            return right_ans if right_ans is not None else -1        
        else:
            left_ans = self.binary_search(nums, 0, index, target)
            return left_ans if left_ans is not None else -1
        
    def find_maximum(self, nums):
        maximum = nums[0]
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r)>>1
            if nums[mid] < maximum:
                r = mid - 1
            else:
                l = mid + 1
                maximum = nums[mid]
        return l-1
    
    def binary_search(self, nums, l, r, target):
        while l <= r:
            mid = (l+r) >> 1
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        

print(Solution().search([4,5,6,7,0,1,2], 4))
print(Solution().search([8,9,0,1,2,3,4,5], 0))
print(Solution().search([4,5,6,7,8,9,1,2], 5))
print(Solution().search([2,1], 0))


    
    