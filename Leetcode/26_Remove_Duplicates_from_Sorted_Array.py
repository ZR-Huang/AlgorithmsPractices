'''
For this problem, we should notice that the nums list have to be
modified when compute the length of nums.

Thus, I use double-pointer method that use first pointer (l) to 
indicate the last unique element and second pointer (r) to 
indicate the current element.

If element indicated by r (r-element) is same as l-element, 
I move the pointer r to the next. If r-elemnt is different to 
l-element, first move the pointer l to the next for the extra space 
to store new unique element, then change the l-element and r-element, 
and move pointer r to the next.
'''
class Solution:
    def removeDuplicates(self, nums) -> int:
        l = 0 # first pointer
        r = 1 # second pointer
        while r < len(nums):
            if nums[l] == nums[r]:
                r += 1
            else:
                l += 1
                nums[l], nums[r] = nums[r], nums[l]
                r += 1
        
        # print(nums)
        return l+1
        

print(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))