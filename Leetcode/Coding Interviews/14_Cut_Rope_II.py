'''
与前一题相同，多了一个大数求余的问题
问题规模
2 <= n <= 1000
'''
class Solution:
    def cuttingRope(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[1] = 1
        for i in range(2, n+1):
            _maximum = 0
            for j in range(1, i):
                _maximum = max([_maximum, j * (i - j), j * dp[i-j]])
            dp[i] = _maximum 
        return int(dp[-1] % int(1e9+7))

    def cuttingRope(self, n: int) -> int:
        if n <= 3 : return n - 1
        a, b, p, x, rem = n // 3 - 1, n % 3, int(1e9+7), 3, 1
        while a > 0: # 求 rem = 3^(a-1) % p
            if a % 2: rem = (rem * x) % p
            x = x ** 2 % p 
            a //= 2
        if b == 0: return (rem * 3) % p # 3^a % p
        if b == 1: return (rem * 4) % p # 3^(a-1) * 4 % p
        return (rem * 6) % p # 3^a * 2 % p = 3 ^(a-1) *6 %p