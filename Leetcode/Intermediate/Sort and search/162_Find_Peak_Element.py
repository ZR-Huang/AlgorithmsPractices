'''
A peak element is an element that is greater than its neighbors.
Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.
The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
You may imagine that nums[-1] = nums[n] = -∞.

Example 1:
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:
Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5 
Explanation: Your function can return either index number 1 where the peak element is 2, 
             or index number 5 where the peak element is 6.

Note:
Your solution should be in logarithmic complexity.
'''
from typing import List
class Solution:
    def findPeakElement_v1(self, nums: List[int]) -> int:
        """
        Time : O(N)
        """
        if len(nums) == 1:
            return 0
        # ans = 0
        for i, value in enumerate(nums):
            if i == 0:
                if value > nums[i+1]:
                    return i
            elif i == len(nums)-1:
                if value >= nums[i-1]:
                    return i
            else:
                if value >= nums[i-1] and value > nums[i+1]:
                    return i
    
    def findPeakElement_v2(self, nums: List[int]) -> int:
        """
        Optimized version
        """
        for i, value in enumerate(nums):
            if nums[i]>nums[i+1]:
                return i
        return len(nums)-1


    def findPeakElement_v3(self, nums: List[int]) -> int:
        """Binary search
        """
        if len(nums) == 1:
            return 0
        ans = 0
        def binary_search(nums, l, r):
            nonlocal ans
            if l > r:
                return
            mid = (l+r) >> 1
            if mid == len(nums)-1 and nums[mid] >= nums[mid-1]:
                ans = mid
            elif mid == 0 and nums[mid] > nums[mid+1]:
                ans = mid
            elif nums[mid] > nums[mid+1] and nums[mid] >= nums[mid-1]:
                ans = mid
            elif nums[mid] <= nums[mid+1]:
                binary_search(nums, mid+1, r)
            elif nums[mid] < nums[mid-1]:
                binary_search(nums, l, mid-1)
            
        binary_search(nums, 0, len(nums)-1)
        return ans

    def findPeakElement_v4(self, nums: List[int]) -> int:
        """
        Optimized version (recusive solution)
        """
        def binary_search(nums, l, r):
            if l == r:
                return l
            mid = (l+r) >> 1
            if nums[mid] > nums[mid+1]:
                return binary_search(nums, l, mid)
            else:
                return binary_search(nums, mid+1, r)    
        
        return binary_search(nums, 0, len(nums)-1)

    def findPeakElement_v5(self, nums: List[int]) -> int:
        """
        Optimized version (iterative solution)
        """
        def binary_search(nums, l, r):
            while True:
                if l == r:
                    return l
                mid = (l+r) >> 1
                if nums[mid] > nums[mid+1]:
                    r = mid
                else:
                    l = mid + 1 
        
        return binary_search(nums, 0, len(nums)-1)
        