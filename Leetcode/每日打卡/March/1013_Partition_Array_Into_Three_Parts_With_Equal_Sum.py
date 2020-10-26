'''
Given an array A of integers, return true if and only if we can partition the array into 
three non-empty parts with equal sums.

Formally, we can partition the array if we can find indexes i+1 < j 
with (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1])

Example 1:
Input: A = [0,2,1,-6,6,-7,9,1,2,0,1]
Output: true
Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1

Example 2:
Input: A = [0,2,1,-6,6,7,9,-1,2,0,1]
Output: false

Example 3:
Input: A = [3,3,6,5,-2,2,5,1,-9,4]
Output: true
Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4

Constraints:
- 3 <= A.length <= 50000
- -10^4 <= A[i] <= 10^4
'''
from typing import List
class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        for l in range(1, len(A)-1):
            for r in range(l+1, len(A)):
                if (sum(A[:l])==sum(A[l:r])) and (sum(A[l:r])==sum(A[r:])):
                    return True
        return False

    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        sum_ = sum(A)
        if sum_%3 != 0:
            return False

        target_of_part = sum_ // 3
        i, length = 1, len(A)
        j, sum_left, sum_right = length-1, A[0], A[-1]
        while i < j: # 中间的部分必须非空
            if sum_left == target_of_part and sum_right==target_of_part:
                return True
            if sum_left != target_of_part:
                sum_left+=A[i]
                i+=1
            if sum_right!=target_of_part:
                j-=1
                sum_right+=A[j]
        return False

print(Solution().canThreePartsEqualSum([18,12,-18,18,-19,-1,10,10]))
print(Solution().canThreePartsEqualSum([0,2,1,-6,6,-7,9,1,2,0,1]))
print(Solution().canThreePartsEqualSum([0,2,1,-6,6,7,9,-1,2,0,1]))
print(Solution().canThreePartsEqualSum([3,3,6,5,-2,2,5,1,-9,4]))