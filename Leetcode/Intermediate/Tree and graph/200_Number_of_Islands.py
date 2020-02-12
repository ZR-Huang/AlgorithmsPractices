'''
Given a 2d grid map of '1's (land) and '0's (water), 
count the number of islands. An island is surrounded 
by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input:
11110
11010
11000
00000
Output: 1

Example 2: 
Input:
11000
11000
00100
00011
Output: 3
'''
from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        Time limitation exceeded
        '''
        def bfs(i, j, grid):
            q = deque()
            visited = set()
            q.append((i,j))
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            while q:
                curr_i, curr_j = q.popleft()
                visited.add((curr_i, curr_j))
                for dx, dy in directions:
                    if (0<=curr_i+dx<m) and (0<=curr_j+dy<n):
                        if grid[curr_i+dx][curr_j+dy]=='1' and ((curr_i+dx, curr_j+dy) not in visited):
                            q.append((curr_i+dx, curr_j+dy))
            return visited
        
        if not grid:
            return 0
        ans = 0
        visited = set()
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1' and ((i, j) not in visited):
                    visited.update(bfs(i, j, grid))
                    ans += 1
        
        return ans

    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        Pass.
        The island nodes should be marked as '0' before enqueuing, 
        and otherwise it might result in the same node enqueues repeatedly.
        '''
        def bfs(i, j,m,n, grid):
            q = deque()
            q.append((i,j))
            while q:
                curr_i, curr_j = q.popleft()
                if curr_i-1>=0 and grid[curr_i-1][curr_j]=='1':
                    q.append((curr_i-1, curr_j))
                    grid[curr_i-1][curr_j] = '0'
                if curr_i+1<m and grid[curr_i+1][curr_j]=='1':
                    q.append((curr_i+1, curr_j))
                    grid[curr_i+1][curr_j] = '0'
                if curr_j-1>=0 and grid[curr_i][curr_j-1]=='1':
                    q.append((curr_i, curr_j-1))
                    grid[curr_i][curr_j-1] = '0'
                if curr_j+1<n and grid[curr_i][curr_j+1]=='1':
                    q.append((curr_i, curr_j+1))
                    grid[curr_i][curr_j+1] = '0'
        
        if not grid:
            return 0
        ans = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    grid[i][j] = '0'
                    bfs(i, j,m, n, grid)
                    ans += 1
        
        return ans