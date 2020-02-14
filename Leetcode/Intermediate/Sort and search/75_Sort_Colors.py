'''
Given an array with n objects colored red, white or blue, 
sort them in-place so that objects of the same color are adjacent, 
with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.
Example:
Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Follow up:
- A rather straight forward solution is a two-pass algorithm using counting sort.
  First, iterate the array counting number of 0's, 1's, and 2's, 
  then overwrite array with total number of 0's, then 1's and followed by 2's.
- Could you come up with a one-pass algorithm using only constant space?
'''
from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        
        self.quicksort(nums)
    
    def _quick_sort_(self, nums: List[int], left, right) -> None:
        if left >= right:
            return
        
        pivot_index = self.partition(nums, left, right)
        self._quick_sort_(nums, left, pivot_index-1)
        self._quick_sort_(nums, pivot_index+1, right)
    
    def partition(self, nums, start, end):
        l = r = start
        while r < end:
            if nums[r] <= nums[end]:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            r += 1
        nums[l], nums[end] = nums[end], nums[l]
        return l
    
    def quicksort(self, nums):
        self._quick_sort_(nums, 0, len(nums)-1)


    def sortColors_v2(self, nums: List[int]) -> None:
        """
        This version is similar to the partition part of the quick sort
        """
        l, curr, r = 0, 0, len(nums)-1
        while curr <= r:
            if nums[curr] == 2:
                nums[curr], nums[r] = nums[r], nums[curr]
                r -= 1
            elif nums[curr] == 0:
                nums[curr], nums[l] = nums[l], nums[curr]
                l += 1
                curr += 1
            else:
                curr += 1

nums = [0]
print(Solution().sortColors_v2(nums))