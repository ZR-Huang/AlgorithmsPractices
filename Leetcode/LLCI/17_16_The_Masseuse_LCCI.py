'''
A popular masseuse receives a sequence of back-to-back appointment requests and 
is debating which ones to accept. She needs a break between appointments and 
therefore she cannot accept any adjacent requests. Given a sequence of back-to-back 
appoint­ ment requests, find the optimal (highest total booked minutes) set the masseuse can honor. 
Return the number of minutes.

Note: This problem is slightly different from the original one in the book.

Example 1:
Input:  [1,2,3,1]
Output:  4
Explanation:  Accept request 1 and 3, total minutes = 1 + 3 = 4

Example 2:
Input:  [2,7,9,3,1]
Output:  12
Explanation:  Accept request 1, 3 and 5, total minutes = 2 + 9 + 1 = 12

Example 3:
Input:  [2,1,4,5,3,1,1,3]
Output:  12
Explanation:  Accept request 1, 3, 5 and 8, total minutes = 2 + 4 + 3 + 3 = 12
'''
class Solution: # 跟rob house的题目类似
    def massage(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0 or n == 1:
            return nums[0] if nums else 0
        dp = [0]*n
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        return dp[-1]