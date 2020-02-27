'''
找出数组中重复的数字。
在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。
数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。
请找出数组中任意一个重复的数字。

示例 1：
输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3 
 

限制：
2 <= n <= 100000
'''

# Here is a solution to the problem on LeetCode

class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        """
        This time and space complexity are O(n) and O(n) respectively.
        """
        # create a hashmap for the nums array
        hashmap = [-1 for _ in range(len(nums))]
        for n in nums:
            if hashmap[n] != -1:
                return n
            else:
                hashmap[n] = 1

    # if the nums is sorted
    def findRepeatNumber_v2(self, nums: List[int]) -> int:
        """
        We note the nums in the array range from 0~n-1.
        If there is no duplication, the number i will be arranged 
        at the index i after sorting the array.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        if len(nums) <= 0:
            return -1
        
        for num in nums:
            if num < 0 or num > len(nums)-1:
                return -1
        
        # Step 1. Traversal the array
        for i in range(len(nums)):
            while nums[i] != i:
                # when the nums not in the right position,
                # we check the nums[nums[i]]
                if nums[i] == nums[nums[i]]:
                    # duplication[0] = nums[i]
                    return num[i]
                # Step 2. swap nums[i] and nums[nums[i]] to 
                # arrange the num into the right position
                tmp = nums[i]
                nums[i] = nums[nums[i]]
                nums[tmp] = tmp

        return -1
