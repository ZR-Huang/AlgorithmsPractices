'''
从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。
2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。

示例 1:
输入: [1,2,3,4,5]
输出: True

示例 2:
输入: [0,0,1,2,5]
输出: True
 
限制：
- 数组长度为 5 
- 数组的数取值为 [0, 13] .
'''
from typing import List

class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        zeroCount , i = 0 , 0
        while i<5 and nums[i]==0:
            zeroCount += 1
            i+=1
        if i >= 5:
            return True
        pre = nums[i]
        i+= 1
        while i < 5:
            if nums[i]==pre+1:
                pre = nums[i]
                i += 1
            elif nums[i] > pre+1 and zeroCount > 0:
                zeroCount-=1
                pre = pre + 1
            elif nums[i] > pre+1 and zeroCount <= 0:
                return False
            elif nums[i] < pre+1:
                return False
        return True

    def isStraight_v2(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        zeroCount, i = 0, 0
        while i<5 and nums[i]==0:
            zeroCount+=1
            i+=1
        if i>=5:
            return True
        
        while i<4:
            if nums[i+1]-nums[i]==1:
                i+=1
            elif (nums[i+1]-nums[i]>1 and nums[i+1]-nums[i]-1 <= zeroCount):
                zeroCount -= nums[i+1]-nums[i]-1
                i+=1
            elif (nums[i+1]-nums[i]>1 and nums[i+1]-nums[i]-1 > zeroCount) or (nums[i+1]-nums[i]<1):
                return False
        return True

    def isStraight_v3(self, nums: List[int]) -> bool:
        visited = set()
        maxValue = 0
        minValue = 15
        for n in nums:
            if n not in visited:
                visited.add(n)
                if n != 0:
                    maxValue = maxValue if maxValue >= n else n
                    minValue = minValue if minValue <= n else n
            else:
                return False
        return True if maxValue - minValue + 1 <= 5 else False
        
        