'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:
nums1 = [1, 3]
nums2 = [2]
The median is 2.0

Example 2:
nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5
'''

from typing import List

class Solution :
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def getKthElement(k):
            index1, index2 = 0, 0
            while True:
                if index1 == m:
                    return nums2[index2+k-1]
                if index2 == n:
                    return nums1[index1+k-1]
                if k == 1:
                    return min(nums1[index1], nums2[index2])
                
                newIndex1 = min(index1 + k //2 - 1, m-1)
                newIndex2 = min(index2 + k //2 - 1, n-1)
                pivot1, pivot2 = nums1[newIndex1], nums2[newIndex2]
                if pivot1 <= pivot2:
                    k -= newIndex1 - index1 + 1
                    index1 = newIndex1 + 1
                else:
                    k -= newIndex2 - index2 + 1
                    index2 = newIndex2 + 1
        
        m, n = len(nums1), len(nums2)
        totalLen = m + n
        if totalLen % 2 == 1:
            return getKthElement((totalLen+1)//2)
        else:
            return (getKthElement(totalLen//2) + getKthElement(totalLen // 2 + 1)) / 2


if __name__ == '__main__':
    print(Solution().findMedianSortedArrays([1,3],[2]))