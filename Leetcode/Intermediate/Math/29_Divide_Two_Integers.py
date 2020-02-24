'''
Given two integers dividend and divisor, divide two integers without using multiplication, 
division and mod operator.
Return the quotient after dividing dividend by divisor.
The integer division should truncate toward zero.

Example 1:
Input: dividend = 10, divisor = 3
Output: 3

Example 2:
Input: dividend = 7, divisor = -3
Output: -2

Note:
- Both dividend and divisor will be 32-bit signed integers.
- The divisor will never be 0.
- Assume we are dealing with an environment which could only store integers within 
    the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose of this problem, 
    assume that your function returns 2^31 − 1 when the division result overflows.
'''
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Time limitation exceeded
        # O(N) n = quotient, traverse all solutions
        OVERFLOW = 2**31 - 1
        if divisor == 0:
            return OVERFLOW
        dividend_sign, divisor_sign = 1, 1
        if dividend < 0:
            dividend = -1*dividend
            dividend_sign = -1
        if divisor < 0:
            divisor = -1* divisor
            divisor_sign = -1
        i = 0
        _sum_ = 0
        while _sum_ < dividend:
            _sum_ += divisor
            i += 1
            if i > OVERFLOW:
                return OVERFLOW
        i = i if _sum_ == dividend else i - 1
        i = dividend_sign * divisor_sign * i
        return i 

    def divide(self, dividend: int, divisor: int) -> int:
        # Binary search
        # O(logN) n = quotient
        OVERFLOW = 2**31 - 1
        if divisor == 0:
            return OVERFLOW
        dividend_sign, divisor_sign = 1, 1
        if dividend < 0:
            dividend = -1*dividend
            dividend_sign = -1
        if divisor < 0:
            divisor = -1* divisor
            divisor_sign = -1

        l, r = 0, dividend
        while l <= r:
            mid = l + ((r - l) >> 1)
            if mid * divisor < dividend:
                l = mid + 1
            elif mid * divisor > dividend:
                r = mid - 1
            else:
                r = mid
                break
        
        r = dividend_sign * divisor_sign * (r)
        return r if r <= OVERFLOW else OVERFLOW

    def divide(self, dividend: int, divisor: int) -> int:
        # Bit Operation
        # O(logN) n = quotient
        # Solution Analysis: https://leetcode-cn.com/problems/divide-two-integers/solution/xiao-xue-sheng-du-hui-de-lie-shu-shi-suan-chu-fa-b/
        INT_MAX = 2**31 - 1
        if divisor == 0:
            return INT_MAX
        dividend_sign, divisor_sign = 1, 1
        if dividend < 0:
            dividend = -1*dividend
            dividend_sign = -1
        if divisor < 0:
            divisor = -1* divisor
            divisor_sign = -1
        
        count = 0
        res = 0
        while divisor <= dividend:
            divisor <<= 1
            count += 1
        while count > 0:
            count -= 1
            divisor >>= 1
            if divisor <= dividend:
                res += 1 << count
                dividend -= divisor
        res = dividend_sign * divisor_sign * res
        return res if res <= INT_MAX else INT_MAX
        
print(Solution().divide(10, 3))