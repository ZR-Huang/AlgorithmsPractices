'''
Implement int sqrt(int x).
Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
Since the return type is an integer, the decimal digits are truncated 
and only the integer part of the result is returned.

Example 1:
Input: 4
Output: 2

Example 2:
Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.
'''

class Solution:
    def mySqrt(self, x: int) -> int:
        # O(sqrt(n))
        i = 1
        while i * i <= x:
            i += 1
        return i - 1

    def mySqrt(self, x: int) -> int:
        # O(log(sqrt(n)))
        l, r = 1, x // 2 + 1 # 1 // 2 = 0, so plus 1.
        while l <= r:
            mid = l + (r - l) // 2
            if mid * mid < x:
                l = mid + 1
            elif mid * mid > x:
                r = mid - 1
            else:
                return mid
        return l - 1
            

print(Solution().mySqrt(4))
print(Solution().mySqrt(8))