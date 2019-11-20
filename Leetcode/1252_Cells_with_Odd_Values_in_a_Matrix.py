class Solution:
    def oddCells(self, n: int, m: int, indices) -> int:
        '''
        According to the rules, operate on the matrix step by step
        '''
        matrix = [[0 for _ in range(m)] for _ in range(n)]
        
        for (row, col) in indices:
            for j in range(len(matrix[row])):
                matrix[row][j] += 1
            for i in range(len(matrix)):
                matrix[i][col] += 1
        # print(matrix)
        result = 0
        for row in matrix:
            for elem in row:
                if elem % 2:
                    result += 1
        return result


print(Solution().oddCells(2,3,[[0,1],[1,1]]))