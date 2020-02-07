'''
Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:
Return true if there exists i, j, k 
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.

Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.

Example 1:
Input: [1,2,3,4,5]
Output: true

Example 2:
Input: [5,4,3,2,1]
Output: false
'''

class Solution:
    def increasingTriplet(self, nums) -> bool:
        """
        the code is wrong, but it could be a reference of 
        the right code. There is a hidden trick between 
        two versions
        """
        triplet = [nums[0], None, None]
        for elem in nums[1:]:
            if (not triplet[1]) and (elem < triplet[0]):
                triplet[0] = elem
            elif (not triplet[1]) or ((not triplet[2]) and (triplet[0] < elem < triplet[1])) :
                triplet[1] = elem
            elif (not triplet[2]) and (elem > triplet[1]):
                print(triplet)
                return True
        
        return False

    def increasingTriplet(self, nums) -> bool:
        """
        trick: we can directly replace the small when meet a value smaller than the small, 
        even if we have already found the increasing subsequence with 2 elements.
        The hidden truth is that there is a previous "minimum" occurs before the mid. Thus, 
        when we meet a value greater than the mid, we still can tell a increaing triplet 
        subsequence exists.
        """
        small = 10**10
        mid = 10**10
        for elem in nums:
            if small >= elem:
                small = elem
            elif mid >= elem:
                mid = elem
            elif mid < elem:
                return True
        
        return False



print(Solution().increasingTriplet([1,2,3,4,5]))
print(Solution().increasingTriplet([5,4,3,2,1]))
print(Solution().increasingTriplet([5,1,2,1,3]))
print(Solution().increasingTriplet([5,1,6,2,7]))
print(Solution().increasingTriplet([2,4,-2,-3]))