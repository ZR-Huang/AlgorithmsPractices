'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:
Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
class Solution:
    def threeSum(self, nums):
        def two_sum(nums, target):
            d = {}
            result = []
            for index, value in enumerate(nums):
                if (target-value) in d:
                    result.append([target-value, value])
                else:
                    d[value] = True

            return result
        
        nums.sort()
        ans = []
        found = set() # store the triplets which are already found.
        for index, a in enumerate(nums):
            if a > 0:
                break # if a > 0, it is impossible that the nums after a meet the requirements
            if index > 0 and nums[index] == nums[index-1]:
                continue # if a equals to the previous element, then jump it to avoid duplicated triplets.

            result = two_sum(nums[index+1:], 0-a)
            if result:
                for b, c in result:
                    # frozenset is immutable and hashable, set is mutable and unhashable
                    triplets = frozenset([a, b, c]) 
                    if triplets not in found:
                        ans.append([a,b,c])
                        found.add(triplets)
        
        return ans


print(Solution().threeSum([0,0,0,0,0,0]))