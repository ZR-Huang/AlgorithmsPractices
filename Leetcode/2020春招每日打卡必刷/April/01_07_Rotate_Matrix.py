'''
与主站的48题相同，../Basic/Array/48_Rotate_Image

Given an image represented by an N x N matrix, where each pixel in the image is 4 bytes, 
write a method to rotate the image by 90 degrees. Can you do this in place?

Example 1:
Given matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],
Rotate the matrix in place. It becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

Example 2:
Given matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 
Rotate the matrix in place. It becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
'''
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if matrix and matrix[0]:
            self.helper(matrix, 0, len(matrix)-1, 0, len(matrix[0])-1)

    def helper(self, matrix, start_i, end_i, start_j, end_j):
        if start_i >= end_i:
            return 
        for i in range(start_i, end_i):
            tmp1 = matrix[i][end_j]
            matrix[i][end_j] = matrix[start_i][i]
            tmp2 = matrix[end_i][-i-1]
            matrix[end_i][-i-1] = tmp1
            tmp1 = matrix[-i-1][start_j]
            matrix[-i-1][start_j] = tmp2
            matrix[start_i][i] = tmp1
        self.helper(matrix, start_i+1, end_i-1, start_j+1, end_j-1)
