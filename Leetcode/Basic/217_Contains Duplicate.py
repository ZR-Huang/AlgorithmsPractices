class Solution:
    def containsDuplicate(self, nums) -> bool:
        d = {} # store the elements which already exist

        for elem in nums:
            if elem in d:
                return True
            else:
                d[elem] = 1

        return False

print(Solution().containsDuplicate([0]))