class Solution:
    def singleNumber(self, nums) -> int:
        d = {}

        for elem in nums:
            if elem in d:
                d[elem] += 1
            else:
                d[elem] = 1

        for key, value in d.items():
            if value == 1:
                return key

print(Solution().singleNumber([4,1,2,1,2]))