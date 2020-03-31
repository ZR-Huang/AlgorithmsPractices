'''
给你一个整数数组 nums，请你将该数组升序排列。

示例 1：
输入：nums = [5,2,3,1]
输出：[1,2,3,5]

示例 2：
输入：nums = [5,1,1,2,0,0]
输出：[0,0,1,1,2,5]

提示：
    1 <= nums.length <= 50000
    -50000 <= nums[i] <= 50000
'''
from typing import List
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums)-1)
        return nums

    def quickSort(self, nums, start, end):
        if start >= end:
            return 
        pivot = self.partition(nums, start, end)
        self.quickSort(nums, start, pivot-1)
        self.quickSort(nums, pivot+1, end)

    def partition(self, nums, start, end):
        l = r = start
        while r < end:
            if nums[r] <= nums[end]: # choose the last element as pivot
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            r += 1
        nums[l], nums[end] = nums[end], nums[l]
        return l    

print(Solution().sortArray([5,1,1,2,0,0]))