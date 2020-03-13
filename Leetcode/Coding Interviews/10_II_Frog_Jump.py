'''
一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。
答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例 1：
输入：n = 2
输出：2

示例 2：
输入：n = 7
输出：21

提示：
0 <= n <= 100
注意：本题与主站 509 题相同：https://leetcode-cn.com/problems/fibonacci-number/
    与《剑指offer》第10题Fibonacci数列也是一样的。
'''
class Solution:
    def numWays(self, n: int) -> int:
        if n==0 or n== 1:
            return 1
        M = 1e9+7
        F = [0]*(n+1)
        F[0], F[1] = 1, 1
        for i in range(2, n+1):
            F[i] = int((F[i-1] + F[i-2]) % M)
        return F[-1]