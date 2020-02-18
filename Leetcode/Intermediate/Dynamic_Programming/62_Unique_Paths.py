'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. 
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
Note: m and n will be at most 100.

Example 1:
Input: m = 3, n = 2   # m: # columns ; n: # rows
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right

Example 2:
Input: m = 7, n = 3
Output: 28
'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*(m+1) for _ in range(n+1)]
        dp[0][1], dp[1][0] = 1, 0
        for i in range(1,n+1):
            for j in range(1, m+1):
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[-1][-1]

    def uniquePaths_v2(self, m: int, n: int) -> int:
        # Optimize space : O(2n)
        pre = [1] * m   # record for previous row
        curr = [1] * m
        for i in range(1,n):
            for j in range(1, m):
                curr[j] = pre[j] + curr[j-1]
            pre = curr[:]
        return curr[-1]

    def uniquePaths_v3(self, m: int, n: int) -> int:
        # Optimize space : O(n)
        curr = [1] * m
        for i in range(1,n):
            for j in range(1, m):
                curr[j] += curr[j-1]
        return curr[-1]

    def uniquePaths_v3(self, m: int, n: int) -> int:
        # Optimize space : O(n)
        curr = [1] * m
        for i in range(1,n):
            for j in range(1, m):
                curr[j] += curr[j-1]
        return curr[-1]

    def uniquePaths_v4(self, m: int, n: int) -> int:
        # 排列组合
        from math import factorial
        return factorial(m+n-2) // factorial(m-1) // factorial(n-1)

print(Solution().uniquePaths_v4(3,2))
print(Solution().uniquePaths_v4(1,2))
print(Solution().uniquePaths_v4(7,3))
