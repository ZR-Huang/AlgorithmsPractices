'''
You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).

Note:
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:
Given input matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

Example 2:
Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
'''
class Solution:
    def rotate(self, matrix):
        def helper(matrix, start_i, end_i, start_j, end_j):
            # when the size of the current matrix is equal or small than 1x1
            if start_i >= end_i: 
                return

            for i in range(start_i, end_i):
                '''
                one iteration:
                1 2 3               1 2 1           1 2 1           1 2 1           7 2 1
                4 5 6               4 5 6           4 5 6           4 5 6           4 5 6
                7 8 9 tmp=None ->   7 8 9 tmp=3 ->  7 8 3 tmp=9 ->  9 8 3 tmp=7 ->  9 8 3 tmp=1
                '''
                tmp1 = matrix[i][end_j]
                matrix[i][end_j] = matrix[start_i][i]
                tmp2 = matrix[end_i][-i-1]
                matrix[end_i][-i-1] = tmp1
                tmp1 = matrix[-i-1][start_j]
                matrix[-i-1][start_j] = tmp2
                matrix[start_i][i] = tmp1
            
            helper(matrix, start_i+1, end_i-1, start_j+1, end_j-1)
        
        if matrix and matrix[0]:
            helper(matrix, 0, len(matrix)-1, 0, len(matrix[0])-1)
