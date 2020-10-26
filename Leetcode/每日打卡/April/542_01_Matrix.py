'''
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.
The distance between two adjacent cells is 1.

Example 1:
Input:
[[0,0,0],
 [0,1,0],
 [0,0,0]]
Output:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Example 2:
Input:
[[0,0,0],
 [0,1,0],
 [1,1,1]]
Output:
[[0,0,0],
 [0,1,0],
 [1,2,1]]

Note:
    The number of elements of the given matrix will not exceed 10,000.
    There are at least one 0 in the given matrix.
    The cells are adjacent in only four directions: up, down, left and right.
'''
from typing import List
from collections import deque
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix[0]:
            return matrix
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0:
                    matrix[i][j] = self.nearestZero(matrix, i, j, m, n)
        return matrix
        
    def nearestZero(self, matrix, x, y, m, n):
        q = deque()
        q.append((x,y))
        visited = set()
        visited.add((x,y))
        directs = [(-1,0), (1,0), (0,-1), (0,1)]
        distance = -1
        while q:
            length = len(q)
            distance += 1
            for _ in range(length):
                i, j = q.popleft()
                if matrix[i][j] == 0:
                    return distance
                for dx, dy in directs:
                    if 0<= i+dx<m and 0<=j+dy<n and (i+dx, j+dy) not in visited:
                        q.append((i+dx, j+dy))

    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix[0]:
            return matrix
        m, n = len(matrix), len(matrix[0])
        dist = [[0]* n for _ in range(m)]
        q = deque()
        visited = set()
        # 把所有0添加进队列
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    q.append((i, j))
                    visited.add((i, j))
        
        # BFS
        directs = [(-1,0), (1,0), (0,-1), (0,1)]
        while q:
            i,j = q.popleft()
            for dx, dy in directs:
                if 0<= i+dx<m and 0<=j+dy<n and (i+dx, j+dy) not in visited:
                    dist[i+dx][j+dy] = dist[i][j] + 1
                    q.append((i+dx, j+dy))
                    visited.add((i+dx, j+dy))
        return dist

                
print(Solution().updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))
