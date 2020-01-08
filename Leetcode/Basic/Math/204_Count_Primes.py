'''
Count the number of prime numbers less than a non-negative number, n.

Example:
Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
'''

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        ans = 1 # 2 is prime
        for num in range(3, n):
            # if num is even, it can be skipped
            if num & 1 == 0:
                continue
            elif self.is_prime(num):
                ans += 1
        return ans

    def is_prime(self, n):
        i = 2
        while i*i <= n:
            if n % i == 0:
                return False
            i += 1
        return True

    def sieve_of_eratosthenes(self, n):
        if n < 3:
            return 0

        is_prime = [1] * n
        is_prime[0], is_prime[1] = 0, 0
        
        i = 2
        while i * i < n:
            if not is_prime[i]:
                i += 1
                continue
            j = i * i
            while j < n:
                is_prime[j] = 0
                j += i
            i += 1
        
        return sum(is_prime)


print(Solution().sieve_of_eratosthenes(20))