class Solution:
    def moveZeroes(self, nums) -> None:
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                break
            i += 1

        j = i + 1
        while j < len(nums):
            if nums[j] != 0:
                break
            j += 1
            
        while j < len(nums):
            if nums[i] == 0 and nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            else:
                if nums[i] != 0:
                    i += 1
                if nums[j] == 0:
                    j += 1

        
nums = [1,1,0,3,12]
Solution().moveZeroes(nums)
print(nums)