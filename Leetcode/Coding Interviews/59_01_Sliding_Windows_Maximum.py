'''
注意：本题与主站 239 题相同：https://leetcode-cn.com/problems/sliding-window-maximum/

给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。

示例:
输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7] 
解释: 
  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
 
提示：
你可以假设 k 总是有效的，在输入数组不为空的情况下，1 ≤ k ≤ 输入数组的大小。
'''
from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        if not nums:
            return res
        for i in range(len(nums)-k+1):
            res.append(max(nums[i:i+k]))
        return res

    def maxSlidingWindow_v2(self, nums: List[int], k: int) -> List[int]:
        # 单调队列
        res = []
        q = deque()
        for i, j in zip(range(1-k, len(nums)+1-k), range(len(nums))):
            if i > 0 and q[0] == nums[i-1]:
                q.popleft()
            while q and q[-1] < nums[j]:
                q.pop()
            q.append(nums[j])
            if i>=0 : 
                res.append(q[0])
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.maxSlidingWindow_v2([1,3,1,2,0,5], 3))