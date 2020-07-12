'''
把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。

你需要用一个浮点数数组返回答案，其中第 i 个元素代表这 n 个骰子所能掷出的点数集合中第 i 小的那个的概率。

示例 1:
输入: 1
输出: [0.16667,0.16667,0.16667,0.16667,0.16667,0.16667]

示例 2:
输入: 2
输出: [0.02778,0.05556,0.08333,0.11111,0.13889,0.16667,0.13889,0.11111,0.08333,0.05556,0.02778]

限制：
1 <= n <= 11
'''
from typing import List

class Solution:
    def twoSum(self, n: int) -> List[float]:
        # 递归搜索
        mem = {}
        def count(n, s):
            if n == 1:
                return 1
            if (str(n)+','+str(s)) in mem:
                return mem[str(n)+','+str(s)]
            res = 0
            for i in range(1, 7):
                if s-i >= 1 and s-i <= (n-1)*6 :
                    res += count(n-1, s-i)
            mem[str(n)+','+str(s)] = res
            return res
        
        res = []
        total = 6**n
        for s in range(n, 6*n+1):
            res.append(count(n, s) / total)
        return res

    def twoSumDP(self, n):
        dp = [[0] * (6*n+1) for _ in range(n+1)]
        for i in range(1, 7):
            dp[1][i] = 1
        
        for i in range(2, n+1):
            for s in range(i, 6*i+1):
                for j in range(1, 7):
                    if s-j >= 1 and s-j <= (i-1)*6:
                        dp[i][s] += dp[i-1][s-j]
        
        total = 6 ** n
        for index, v in enumerate(dp[-1]):
            dp[-1][index] = v / total
        return dp[-1][n:]


    def twoSumDP_1D_Space(self, n):
        dp = [0] * (6*n+1)
        for i in range(1, 7):
            dp[i] = 1
        
        for i in range(2, n+1):
            for s in range(6*i, i-1, -1):
                dp[s] = 0
                for j in range(1, 7):
                    if s-j >= i-1 and s-j <= (i-1)*6:
                        dp[s] += dp[s-j]
        
        total = 6 ** n
        for index, v in enumerate(dp):
            dp[index] = v / total
        return dp[n:]
