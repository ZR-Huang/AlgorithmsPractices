'''
输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。

序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

Example 1:
Input: target = 9
Output: [[2,3,4],[4,5]]

Example 2:
Input: target = 15
Output: [[1,2,3,4,5],[4,5,6],[7,8]]

Constraints:
- 1 <= target <= 10^5
'''
from typing import List
class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        # backtrack
        # time : O((0.5n)^2)
        # space : O(n/2)
        def backtrack(sum_, target, curr, arr):
            for i in range(curr+1, target//2 + 1 + 1):
                if sum_ + i > target or i > arr[-1] + 1:
                    break
                elif sum_ + i < target:
                    arr.append(i)
                    backtrack(sum_+i, target, i, arr)
                    arr.pop()
                else:
                    arr.append(i)
                    ans.append(arr.copy())
        
        ans = []
        for i in range(1, target // 2 + 1):
            backtrack(i, target, i, [i])
        
        return ans

    def findContinuousSequence(self, target: int) -> List[List[int]]:
        # sliding window
        # time : O(target)
        # space : O(target)
        ans, window, sum_ = [], [], 0
        for j in range(1, target // 2 + 2):
            while sum_ + j > target:
                sum_ -= window.pop(0)
            if sum_ + j < target:
                sum_ += j
                window.append(j)
            elif sum_ + j == target:
                sum_ += j
                window.append(j)
                ans.append(window.copy())
        return ans

    def findContinuousSequence(self, target: int) -> List[List[int]]:
        # double pointers
        # time : O(target)
        # space : O(1)
        ans, l, r = [], 1, 2
        while l < r:
            sum_ = int((l + r)*(r-l+1) * 0.5)
            if sum_ == target:
                ans.append([i for i in range(l, r+1)])
                l += 1
            elif sum_ > target:
                l += 1
            else:
                r += 1
            
        return ans

    def findContinuousSequence(self, target: int) -> List[List[int]]:
        # enumerate + math
        # time : O(target)
        # space : O(1)
        # analysis : https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/solution/mian-shi-ti-57-ii-he-wei-sde-lian-xu-zheng-shu-x-2/
        ans = []
        for x in range(1, target // 2 + 1):
            delta = 1 - 4 * (x - x * x - 2 * target)
            if delta < 0:
                continue
            delta_sqrt = int(delta ** 0.5)
            if (delta_sqrt * delta_sqrt == delta) and (delta_sqrt - 1) % 2 == 0:
                y = (-1 + delta_sqrt) // 2
                if x < y:
                    ans.append([i for i in range(x, y+1)])
        return ans


print(Solution().findContinuousSequence(9))
print(Solution().findContinuousSequence(15))
print(Solution().findContinuousSequence(50252))