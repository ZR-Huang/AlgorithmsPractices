class Solution:
    def maxArea(self, height):
        l = 0 # left pointer
        r = len(height) - 1 # right pointer
        max_water = 0
        while l != r:
            temp = min(height[l], height[r])*(r - l)
            if temp > max_water:
                max_water = temp
            
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        
        return max_water

print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))