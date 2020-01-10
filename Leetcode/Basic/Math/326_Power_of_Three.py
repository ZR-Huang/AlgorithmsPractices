'''
Given an integer, write a function to determine if it is a power of three.

Example 1:
Input: 27
Output: true

Example 2:
Input: 0
Output: false

Example 3:
Input: 9
Output: true

Example 4:
Input: 45
Output: false

Follow up:
Could you do it without using any loop / recursion?
'''

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # 84ms
        if n <= 0:
            return False
        
        while n != 1:
            if n % 3 == 0:
                n = n // 3
            else:
                return False
        
        return True

    def isPowerOfThree_v2(self, n: int) -> bool:
        # 108ms
        if n <= 0:
            return False
        
        import math
        exponent = math.log(n, 3) # python calculate as log2(n) / log2(3)
        # the result may have the error, such as math.log(243, 3) is 4.999999
        
        # validate if the exponent is an integer.
        epsilon = 0.0000001
        return (exponent + epsilon) % 1 <= 2 * epsilon
    

    def isPowerOfThree_v3(self, n: int) -> bool:
        # 72ms
        # limitation of the integer
        # get the maximum value of the integer
        max_int = 2**31 - 1
        # get the maximum value of the n
        # 3**(math.floor(math.log(max_int, 3))) = 3**math.floor(19.56) = 3**19 = 1162261467
        max_n = 1162261467

        # divisors of max_n are only 3**0, 3**1, ..., 3**19, because three is prime.
        # Hence, if 3**19 % n == 0, n is the power of three.
        return n > 0 and max_n % n == 0