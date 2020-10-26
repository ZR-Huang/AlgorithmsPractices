'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it is able to trap after raining.

Example:
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        # 可以把问题看作是投影，积水的后模型类似左右两侧向最高处的投影
        # 因此左侧和右侧均可以看作一个不严格递增
        # 从前往后
        increment_index, water, last_height = [], 0, 1 # 基准
        for i, h in enumerate(height):
            if h >= last_height:
                increment_index.append(i)
                last_height = h
        for j in range(len(increment_index)-1):
            for i in range(increment_index[j], increment_index[j+1]):
                water += (height[increment_index[j]]-height[i])
        # 从后往前
        last_height = 1
        stop = increment_index[-1]-1 if increment_index else -1
        increment_index.clear()
        for i in range(len(height)-1, stop, -1):
            if height[i] >= last_height:
                increment_index.append(i)
                last_height = height[i]
        for j in range(len(increment_index)-1):
            for i in range(increment_index[j], increment_index[j+1], -1):
                water += (height[increment_index[j]]-height[i])
        return water

    def trap(self, height: List[int]) -> int:
        # 双指针优化
        # https://leetcode-cn.com/problems/trapping-rain-water/solution/jie-yu-shui-by-leetcode/
        left_max, right_max, left, right, water = 0, 0, 0, len(height)-1, 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += (left_max-height[left])
                    left += 1
            else:
                if height[right]>=right_max:
                    right_max = height[right]
                else:
                    water += (right_max-height[right])
                    right -= 1
        return water