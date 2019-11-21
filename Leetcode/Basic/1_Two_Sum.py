class Solution:
    def twoSum(self, nums, target: int):
        # nums = sorted(nums)
        i = 0
        j = len(nums)-1
        while i <= j:
            if nums[i] + nums[j] == target:
                return [i, j]
            elif (nums[i] + nums[j] > target and nums[i]<nums[j]) or \
                (nums[i] + nums[j] < target and nums[i]>nums[j]):
                j -= 1
            elif (nums[i] + nums[j] > target and nums[i]>nums[j]) or \
                (nums[i] + nums[j] < target and nums[i]<nums[j]):
                i += 1
            


print(Solution().twoSum([2, 11, 7, -1, -2, 11, 15], 0))
        