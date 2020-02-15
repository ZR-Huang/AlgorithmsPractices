'''
Find the kth largest element in an unsorted array. 
Note that it is the kth largest element in the sorted order, 
not the kth distinct element.

Example 1:
Input: [3,2,1,5,6,4] and k = 2
Output: 5

Example 2:
Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4

Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
'''

from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Time complexity: O(NlogK)
        Space : O(K)
        """
        left = lambda i: i * 2 + 1
        right = lambda i: i * 2 + 2
        parent = lambda i: (i - 1) // 2
        def heapify(arr, curr_pos, max_pos):
            m_pos, l, r = curr_pos, left(curr_pos), right(curr_pos)
            while l < max_pos:
                if l < max_pos and arr[l] < arr[m_pos]:
                    m_pos = l
                if r < max_pos and arr[r] < arr[m_pos]:
                    m_pos = r
                if m_pos != curr_pos:
                    arr[m_pos], arr[curr_pos] = arr[curr_pos], arr[m_pos]
                    curr_pos = m_pos
                    l, r = left(curr_pos), right(curr_pos)
                else:
                    break
            return arr

        if not nums:
            return -1

        heap = nums[:k]
        curr_pos = parent(len(heap)-1)
        while curr_pos >= 0:
            heap = heapify(heap, curr_pos, k)
            curr_pos -= 1
        
        for i in range(k, len(nums)):
            if nums[i] > heap[0]:
                heap[0] = nums[i]
                heap = heapify(heap, 0, k)
        
        return heap[0]

    def findKthLargest_v2(self, nums: List[int], k: int) -> int:
        """
        Quick selection
        Time : the average time is O(N), the worst time is O(N^2)
        Space: O(1)
        """
        pass

print(Solution().findKthLargest([7,6,5,4,3,2,1], 5))
print(Solution().findKthLargest([3,2,1,5,6,4], 2))
print(Solution().findKthLargest([3,2,3,1,2,4,5,5,6], 4))
