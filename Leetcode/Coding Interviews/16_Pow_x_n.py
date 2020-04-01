'''
注意：本题与主站 50 题相同：https://leetcode-cn.com/problems/powx-n/

实现函数double Power(double base, int exponent)，求base的exponent次方。不得使用库函数，同时不需要考虑大数问题。

示例 1:
输入: 2.00000, 10
输出: 1024.00000

示例 2:
输入: 2.10000, 3
输出: 9.26100

示例 3:
输入: 2.00000, -2
输出: 0.25000
解释: 2-2 = 1/2^2 = 1/4 = 0.25

说明:
    -100.0 < x < 100.0
    n 是 32 位有符号整数，其数值范围是 [−2^31, 2^31 − 1] 。
'''

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n *= -1
        curr_prod = x
        ans = 1
        while n >= 1:
            if n % 2 == 1:
                ans *= curr_prod
            curr_prod = curr_prod * curr_prod
            n >>= 1
        return ans