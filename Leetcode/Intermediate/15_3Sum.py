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
        def two_sum(nums, fixed_index, target):
            d = {}
            result = []
            for index, value in enumerate(nums):
                if index == fixed_index:
                    continue
                else:
                    if (target-value) in d:
                        result.append([target-value, value])
                        # return [target-value, value]
                    else:
                        d[value] = True

            return result
        
        ans = set()
        found = set() # store the triplets which are already found.
        for index, a in enumerate(nums):
            result = two_sum(nums, index, 0-a)
            if result:
                for b, c in result:
                # b, c = result
                    # frozenset is immutable and hashable, set is mutable and unhashable
                    triplets = frozenset([a, b, c]) 
                    if triplets not in found:
                        ans.add((a, b, c))
                        found.add(triplets)
        
        return list(map(list, ans))


print(Solution().threeSum([3,0,-2,-1,1,2]))