'''
Implement pow(x, n), which calculates x raised to the power n(x^n).

Example 1:
Input: 2.00000, 10
Output: 1024.00000

Example 2:
Input: 2.10000, 3
Output: 9.26100

Example 3:
Input: 2.00000, -2
Output: 0.25000
Explanation: 2^(-2) = 1/(2^2) = 1/4 = 0.25

Note:
- -100.0 < x < 100.0
- n is a 32-bit signed integer, within the range [−2^31, 2^31 − 1]
'''
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # O(n)
        ans = 1
        sign = 1
        if n < 0:
            sign = -1
            n = -1 * n
        for _ in range(n):
            ans *= x
        if sign == -1:
            ans = 1 / ans
        return ans

    def myPow_v2(self, x: float, n: int) -> float:
        # O(logn) recurse and memorize
        def recurse(x: float, n: int, memo: dict):
            if n in memo:
                return memo[n]
            if n == 1:
                memo[n] = x
                return memo[n]
            
            mid = n >> 1
            remain = n - mid
            product = recurse(x, mid, memo) * recurse(x, remain, memo)
            memo[n] = product
            return memo[n]

        sign = 1
        if n < 0:
            sign = -1
            n *= -1
        ans = recurse(x, n, {0:1})
        return ans if sign > 0 else 1 / ans

    def myPow_v3(self, x: float, n: int) -> float:
        # O(logn) loop and memorization 
        if n < 0 :
            x = 1 / x
            n *= -1
        ans = 1
        curr_prod = x
        i = n
        while i >= 1:
            if i % 2 == 1:
                ans = ans * curr_prod
            curr_prod = curr_prod * curr_prod
            i >>= 1
        return ans 
        
import time
start = time.time()
Solution().myPow(2, 100000)
print(f"time:{time.time()- start}")
start = time.time()
Solution().myPow_v2(2, 10)
print(f"time:{time.time()- start}")
start = time.time()
Solution().myPow_v3(2, 100000)
print(f"time:{time.time()- start}")