'''
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:
Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]

Example 2:
Input: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]

Follow up:
- A straight forward solution using O(mn) space is probably a bad idea.
- A simple improvement uses O(m + n) space, but still not the best solution.
- Could you devise a constant space solution?
'''

class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        """
        Idea (direactly with extra spaces):
        1. scan the matrix and store indexes of zeroes.
        2. set rows and columns zeroes.
        """
        m = len(matrix)
        n = len(matrix[0])
        if n == 0 or m == 0:
            return 
        
        indexes = []
        for i, row in enumerate(matrix):
            for j, element in enumerate(row):
                if element == 0:
                    indexes.append((i, j))
        
        # print(indexes)
        for i, j in indexes:
            matrix[i] = [0] * n
            for _i in range(m):
                matrix[_i][j] = 0

    def setZeroes_v2(self, matrix) -> None:
        """
        Idea (a constant space solution):
        1. Scan the matrix.
        2. If meet a zero, label the head elements of this row and this column.
        For example, if matrix[i][j] = 0, set matrix[i][0] and matrix[0][j] INF.
        3. Scan the matrix again. Set rows and columns which have the label to zeroes.
        Bugs:
        The problem does not give the range of elements of the matrix, 
        so the solution easily gets the Wrong Answer if the label isn't set appropriately.
        """
        m = len(matrix)
        n = len(matrix[0])
        if n == 0 or m == 0:
            return 
        
        col_0 = False
        for i in range(m):
            if matrix[i][0] == 0:
                col_0 = True
        
        for i in range(m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        # scan the matrix to find out LABEL,
        # and set rows and columns to zeroes 
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # See if the first row needs to be set to zero
        if matrix[0][0] == 0:
            matrix[0] = [0] * n
        
        # See if the first column needs to be set to zero
        if col_0:
            for i in range(m):
                matrix[i][0] = 0
        

matrix = [[8,3,6,9,7,8,0,6],[0,3,7,0,0,4,3,8],[5,3,6,7,1,6,2,6],[8,7,2,5,0,6,4,0],[0,2,9,9,3,9,7,3]]
Solution().setZeroes_v2(matrix)
print(matrix)