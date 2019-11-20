class Solution:
    def generateMatrix(self, n: int):
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        # print(matrix)

        current_num = 1
        # direct: right, down, left and up
        directs = [(0,1), (1,0), (0,-1), (-1,0)]

        i, j = 0, -1
        index = 0 # for directs
        while 1:
            direct = directs[index]
            i += direct[0]
            j += direct[1]
            while i >=0 and j >= 0 and i < n and j < n:
                if matrix[i][j] == 0:
                    matrix[i][j] = current_num
                    current_num += 1
                    i += direct[0]
                    j += direct[1]
                else:
                    break

            i -= direct[0]
            j -= direct[1]

            index = (index + 1) if index + 1 < 4 else 0
            if current_num > n**2:
                break
        
        return matrix

print(Solution().generateMatrix(4))