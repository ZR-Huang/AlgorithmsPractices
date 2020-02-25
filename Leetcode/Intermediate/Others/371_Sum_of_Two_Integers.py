'''
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example 1:
Input: a = 1, b = 2
Output: 3

Example 2:
Input: a = -2, b = 3
Output: 1
'''
class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0x100000000  # 2^32
        MAX_INT = 0x7FFFFFFF
        MIN_INT = MAX_INT + 1

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) % MASK
            b = carry % MASK
        return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT)