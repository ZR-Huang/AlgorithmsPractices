'''
On a N * N grid, we place some 1 * 1 * 1 cubes.
Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).
Return the total surface area of the resulting shapes.

Example 1:
Input: [[2]]
Output: 10

Example 2:
Input: [[1,2],[3,4]]
Output: 34

Example 3:
Input: [[1,0],[0,2]]
Output: 16

Example 4:
Input: [[1,1,1],[1,0,1],[1,1,1]]
Output: 32

Example 5:
Input: [[2,2,2],[2,1,2],[2,2,2]]
Output: 46

Note:
- 1 <= N <= 50
- 0 <= grid[i][j] <= 50
'''
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        # 因为存在凹点，所以侧面积的方法不行
        m, n = len(grid), len(grid[0])
        directs = [(-1,0), (1,0), (0, -1), (0,1)]
        surface = 0 
        for x in range(m):
            for y in range(n):
                for dx, dy in directs:
                    if 0<=x+dx<m and 0<=y+dy<n:
                        if grid[x][y] >= grid[x+dx][y+dy]:
                            surface += grid[x][y] - grid[x+dx][y+dy]
                    else:
                        surface += grid[x][y]
                surface += 2 if grid[x][y] != 0 else 0
        return surface