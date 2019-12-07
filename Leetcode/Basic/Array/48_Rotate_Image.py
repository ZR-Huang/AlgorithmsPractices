class Solution:
    def rotate(self, matrix):
        length = len(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j], matrix[j][length-1-i] = matrix[j][length-1-i], matrix[i][j]
    
matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

Solution().rotate(matrix)
print(matrix)

matrix = [
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]
Solution().rotate(matrix)
print(matrix)