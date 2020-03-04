'''
The Fibonacci numbers, commonly denoted F(n) form a sequence, 
called the Fibonacci sequence, such that each number is 
the sum of the two preceding ones, starting from 0 and 1. That is,
F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.

Given N, calculate F(N).

Example 1:
Input: 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

Example 2:
Input: 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

Example 3:
Input: 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.

Note:
0 ≤ N ≤ 30.
'''
class Solution:
    def fib(self, N: int) -> int:
        # recursive version
        # time : O(2^N)
        # space : O(N)
        if N == 0 or N == 1:
            return N
        return self.fib(N-1)+self.fib(N-2)

    def fib(self, N: int) -> int:
        # memorilize
        # time : O(N)
        # space : O(N+N)
        memo = {0: 0, 1: 1}
        def helper(N, memo):
            if N in memo:
                return memo[N]
            memo[N] = helper(N-1, memo) + helper(N-2, memo)
            return memo[N]
        return helper(N, memo)

    def fib(self, N: int) -> int:
        # iterative version
        # time : O(N)
        # space : O(N)
        if N == 0:
            return 0
        dp = [0] * (N+1)
        dp[1] = 1
        for i in range(2, N+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[N]

    def fib(self, N: int) -> int:
        # iterative version with space optimization
        # time : O(N)
        # space : O(2)
        if N == 0 or N == 1:
            return N
        small, big = 0, 1
        for _ in range(2, N+1):
            tmp = small + big
            small, big = big, tmp
        return big

    def fib(self, N: int) -> int:
        # Matrix Power version
        # time : O(logN)
        # space : O(logN)
        # analysis : https://leetcode-cn.com/problems/fibonacci-number/solution/fei-bo-na-qi-shu-by-leetcode/
        def multiply(A, B):
            x = A[0][0]*B[0][0] + A[0][1]*B[1][0]
            y = A[0][0]*B[0][1] + A[0][1]*B[1][1]
            z = A[1][0]*B[0][0] + A[1][1]*B[1][0]
            w = A[1][0]*B[0][1] + A[1][1]*B[1][1]

            A[0][0], A[0][1], A[1][0], A[1][1] = x, y, z, w
        
        def matrix_power(A, N):
            if N <= 1:
                return A
            matrix_power(A, N // 2)
            multiply(A, A)
            B = [[1,1],[1,0]]
            if N % 2 != 0:
                multiply(A, B)
        
        if N <= 1:
            return N
        A = [[1,1],[1,0]]
        matrix_power(A, N-1)
        return A[0][0]

    def fib(self, N: int) -> int:
        # solve by Binet equation
        # analysis : https://leetcode-cn.com/problems/fibonacci-number/solution/fei-bo-na-qi-shu-by-leetcode/
        golden_ration = (1+5**0.5) / 2
        return int((golden_ration ** N + 1) / 5**0.5)

print(Solution().fib(6))