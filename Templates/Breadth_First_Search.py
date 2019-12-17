'''
This is the solution of the problem of No.167 weekly competition

I think it is the good template of the breadth first search algorithm, 
so archive it in this fold.

1293. Shortest Path in a Grid with Obstacles Elimination
Link: https://leetcode-cn.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/
'''

from collections import deque
class Solution:
    def shortestPath(self, grid, k: int) -> int:
        m, n = len(grid), len(grid[0])
        step = 0 
        direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        q = deque()
        visited = set()
        q.append((0, 0, k))
        visited.add((0, 0, k))

        # Breadth First Search
        while(q):
            size = len(q)
            for _ in range(size):
                i, j, k = q.popleft()
                # visited.add((i,j,k))
                if i == m-1 and j == n-1:
                    return step
                
                for di, dj in direct:
                    ni, nj = i+di, j+dj
                    if ni < 0 or nj < 0 or ni > m-1 or nj > n-1 or (grid[ni][nj]==1 and k<=0):
                        continue
                    
                    if grid[ni][nj] == 1 and (ni,nj,k-1) not in visited:
                        q.append((ni, nj, k-1))
                        visited.add((ni, nj, k-1))
                    elif grid[ni][nj] == 0 and (ni,nj,k) not in visited:
                        q.append((ni, nj, k))
                        visited.add((ni, nj, k))
            step += 1
        
        return -1

grid = [[0,0,1,0,0,0,0,1,0,1,1,0,0,1,1],[0,0,0,1,1,0,0,1,1,0,1,0,0,0,1],[1,1,0,0,0,0,0,1,0,1,0,0,1,0,0],[1,0,1,1,1,1,0,0,1,1,0,1,0,0,1],[1,0,0,0,1,1,0,1,1,0,0,1,1,1,1],[0,0,0,1,1,1,0,1,1,0,0,1,1,1,1],[0,0,0,1,0,1,0,0,0,0,1,1,0,1,1],[1,0,0,1,1,1,1,1,1,0,0,0,1,1,0],[0,0,1,0,0,1,1,1,1,1,0,1,0,0,0],[0,0,0,1,1,0,0,1,1,1,1,1,1,0,0],[0,0,0,0,1,1,1,0,0,1,1,1,0,1,0]]
k = 27
print(Solution().shortestPath(grid, k))