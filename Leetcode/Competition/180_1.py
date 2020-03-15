from typing import List
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        ans = []
        for i in range(m):
            row_min_index = 0
            row_min = 10**5+1
            for j in range(n):
                if matrix[i][j] < row_min:
                    row_min = matrix[i][j]
                    row_min_index = j
            is_max = True
            for k in range(m):
                if matrix[k][row_min_index] > row_min:
                    is_max = False
                    break
            if is_max:
                ans.append(row_min)
        return ans

print(Solution().luckyNumbers([[3,7,8],[9,11,13],[15,16,17]]))
print(Solution().luckyNumbers([[1,10,4,2],[9,3,8,7],[15,16,17,12]]))
print(Solution().luckyNumbers([[7,8],[1,2]]))