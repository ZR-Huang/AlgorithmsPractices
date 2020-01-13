'''
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 2**31.

Example:
Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
'''

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans = 0

        while x != 0 and y != 0:
            if x % 2 != y % 2:
                ans += 1
            
            x >>= 1
            y >>= 1
        
        if x == 0:
            while y != 0:
                ans += 1
                y &= (y-1)
        else:
            while x != 0:
                ans += 1
                x &= (x-1)
        
        return ans

    
    def hammingDistance_v2(self, x, y):
        return bin(x ^ y).count('1')