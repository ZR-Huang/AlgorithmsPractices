'''
注意：本题与主站 343 题相同：https://leetcode-cn.com/problems/integer-break/

给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），
每段绳子的长度记为 k[0],k[1]...k[m] 。请问 k[0]*k[1]*...*k[m] 可能的最大乘积是多少？
例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

示例 1：
输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1

示例 2:
输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36

提示：
2 <= n <= 58
'''
class Solution:
    def cuttingRope(self, n: int) -> int:
        def search(left_len, memo):
            if left_len in memo:
                return memo[left_len]
            _maximum = 0
            for i in range(1, left_len):
                # have to remember compare two options:
                # cut or not cut
                _maximum = max([_maximum, i * (left_len - i), i * search(left_len - i, memo)])
            memo[left_len] = _maximum
            return memo[left_len]
        memo = {1: 1}
        search(n, memo)
        return memo[n]

    def cuttingRope(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[1] = 1
        for i in range(2, n+1):
            _maximum = 0
            for j in range(1, i):
                _maximum = max([_maximum, j * (i - j), j * dp[i-j]])
            dp[i] = _maximum
        return dp[-1]

    def cuttingRope(self, n: int) -> int:
        # greedy
        # analysis : https://leetcode-cn.com/problems/jian-sheng-zi-lcof/solution/mian-shi-ti-14-i-jian-sheng-zi-tan-xin-si-xiang-by/
        import math
        if n<=3:
            return n-1
        a, b = n//3, n % 3
        if b == 0:
            return int(math.pow(3, a))
        if b == 1:
            return int(math.pow(3, a-1) * 4)
        if b == 2:
            return int(math.pow(3, a) * 2)

print(Solution().cuttingRope(8))