'''
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  

示例 1：

输入：[3,4,5,1,2]
输出：1
示例 2：

输入：[2,2,2,0,1]
输出：0
注意：本题与主站 154 题相同：https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/
'''

class Solution:
    def minArray(self, numbers: List[int]) -> int:
        '''
        因为最小值只会出现在右半侧，而且右侧的最后一个元素刚好是旋转数组的分界点。
        所以选择右侧的最后一个元素作为target，存储当前找到的最小元素。
        如果numbers[mid]>target，那么最小值一定在number[mid]的右侧。
        如果numbers[mid]<target, 那么最小值一定在number[mid]的左侧，同时也要更新target值。
        如果numbers[mid]==target,无法确定最小值在哪侧，因此通过改变target值来缩小搜索范围。
        第三种情况涉及比较多的cases，需要去证明。
        '''
        l, r, target = 0, len(numbers)-1, numbers[-1]
        while l < r:
            mid = l + (r-l)//2
            if numbers[mid] > target:
                l = mid+1
            elif numbers[mid]<target:
                target = numbers[mid]
                r = mid
            else:
                r-=1
                target = numbers[r]
        return target