'''
Write an efficient algorithm that searches for a value in an m x n matrix. 
This matrix has the following properties:
- Integers in each row are sorted in ascending from left to right.
- Integers in each column are sorted in ascending from top to bottom.

Example:
Consider the following matrix:
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.
Given target = 20, return false.
'''
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        def binary_search(matrix, target, start, vertical):
            low = start
            high = len(matrix[0])-1 if vertical else len(matrix)-1
            while low <= high:
                mid = (low+high)>>1
                if vertical:
                    if matrix[start][mid] > target:
                        high = mid - 1
                    elif matrix[start][mid] < target:
                        low = mid + 1
                    else:
                        return True
                else:
                    if matrix[mid][start] > target:
                        high = mid - 1
                    elif matrix[mid][start] < target:
                        low = mid + 1
                    else:
                        return True
        
        for i in range(min(len(matrix), len(matrix[0]))):
            if binary_search(matrix, target, i, True) or binary_search(matrix, target, i, False):
                return True
        return False

print(Solution().searchMatrix([[-1,3]], 1))
print(Solution().searchMatrix([[1,1]], 2))
print(Solution().searchMatrix([[-1,3]], 3))
print(Solution().searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 20))
print(Solution().searchMatrix([[1,1]], 1))
print(Solution().searchMatrix([[1,1]], 0))
        