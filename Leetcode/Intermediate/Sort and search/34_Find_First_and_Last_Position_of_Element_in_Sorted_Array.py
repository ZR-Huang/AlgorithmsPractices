'''
Given an array of integers nums sorted in ascending order, 
find the starting and ending position of a given target value.
Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
'''
from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        Binary Search + expand
        The best time is O(logN) and the worst is O(N)
        """
        start, end, l, r = -1, -1, 0, len(nums)-1
        while l <= r:
            mid = (l+r) >> 1
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                start = mid
                break
        
        if start != -1:
            l,r = start, start
            while nums[l] == nums[start] and l >= 0:
                l -= 1
            while nums[r] == nums[start] and r < len(nums):
                r += 1
            start, end = l + 1, r - 1
        return [start, end]

    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        '''
        Binary search twice and the time is O(2logN)
        '''
        def binary_search(nums, l, r, left):
            while l<r:
                mid = (l+r) >> 1
                if nums[mid] > target or (nums[mid]==target and left):
                    r = mid
                else:
                    l = mid + 1
            
            return l
        
        start = binary_search(nums, 0, len(nums), True)
        if nums[start] != target or start == len(nums):
            return [-1, -1]
        
        return [start, binary_search(nums, 0, len(nums), False)]