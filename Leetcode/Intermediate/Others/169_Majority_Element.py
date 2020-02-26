'''
Given an array of size n, find the majority element. 
The majority element is the element that appears 
more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the 
majority element always exist in the array.

Example 1:
Input: [3,2,3]
Output: 3

Example 2:
Input: [2,2,1,1,1,2,2]
Output: 2
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1
        
        for key, count in hashmap.items():
            if count > len(nums) // 2:
                return key
    
    
    # Solution Analysis:
    # https://leetcode-cn.com/problems/majority-element/solution/qiu-zhong-shu-by-leetcode-2/
    def majorityElement(self, nums: List[int]) -> int:
        # Sort
        nums.sort()
        return nums[len(nums) // 2]


    def majorityElement(self, nums: List[int]) -> int:
        # Boyer-Moore Vote
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if candidate == num else -1
        
        return candidate
    