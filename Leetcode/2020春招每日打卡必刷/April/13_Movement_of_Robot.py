'''
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。
一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），
也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。
但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

示例 1：
输入：m = 2, n = 3, k = 1
输出：3

示例 2：
输入：m = 3, n = 1, k = 0
输出：1

提示：
1 <= n,m <= 100
0 <= k <= 20
'''
from collections import deque
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        visited = set()
        # DFS
        # visited.add((0,0))
        # self.move(0, 0, k, m, n, visited)
        # BFS
        q = deque()
        visited.add((0,0))
        q.append((0,0))
        self.search(q, k, m, n, visited)
        return len(visited)

    def digit_sum(self, x):
        sum_ = 0
        while x:
            sum_ += x%10
            x //= 10
        return sum_

    def move(self, x, y, k, m, n, visited):
        directs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directs:
            if (0<=x+dx<m) and (0<=y+dy<n) and ((x+dx, y+dy) not in visited):
                if self.digit_sum(x+dx)+self.digit_sum(y+dy) <=k:
                    visited.add((x+dx, y+dy))
                    self.move(x+dx, y+dy, k, m, n, visited)

    def search(self, q, k, m, n, visited):
        directs = [(1, 0), (0, 1)]
        while q:
            x, y = q.popleft()
            for dx, dy in directs:
                if 0<=x+dx<m and 0<=y+dy<n and ((x+dx, y+dy) not in visited):
                    if self.digit_sum(x+dx)+self.digit_sum(y+dy)<=k:
                        visited.add((x+dx, y+dy))
                        q.append((x+dx, y+dy))
        
print(Solution().movingCount(3,1,0))
print(Solution().movingCount(16,8,4))
print(Solution().movingCount(38,15,9))
print(Solution().movingCount(36,11,15))

