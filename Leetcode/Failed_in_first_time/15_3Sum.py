class Solution:
    def threeSum(self, nums):
        l = 0 # left pointer
        r = len(nums) - 1 # right pointer
        result = []
        d = {} # using to store the middle results

        while l != r:
            if -nums[l] in d:
                result.append(d[-nums[l]].append(nums[l]))
            if -nums[r] in d:
                result.append(d[-nums[r]].append(nums[r]))

            d[nums[l]+nums[r]] = [[nums[l], nums[r]]]
            if nums[l] < nums[r]:
                l += 1
            else:
                r -= 1
        
        print(d)

        return result

print(Solution().threeSum([-1, 0, 1, 2, -1, -4])) 