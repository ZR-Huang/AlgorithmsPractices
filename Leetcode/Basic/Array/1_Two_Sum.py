class Solution:
    def twoSum_v1(self, nums, target):
        # time cost: O(n**2)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

    
    def twoSum_v2(self, nums, target: int):
        # use hashmap
        # time cost: O(n), space cost: O(n)
        '''
        we check whether the target element is in 
        the dict when iterate the nums to insert into the dict.
        '''
        d = {}
        for index, value in enumerate(nums):
            if (target-value) in d:
                return [d[target-value], index]
            else:
                d[value] = index


print(Solution().twoSum_v2([2, 11, 7, -1, -2, 11, 15], 0))
print(Solution().twoSum_v2([3, 2, 4], 6))
print(Solution().twoSum_v2([3, 3, 4, 4, 7], 11))