'''
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: 
Starting with any positive integer, replace the number by the sum of the squares 
of its digits, and repeat the process until the number equals 1 (where it will stay), 
or it loops endlessly in a cycle which does not include 1. 
Those numbers for which this process ends in 1 are happy numbers.

Example: 
Input: 19
Output: true
Explanation: 
1^2 + 9^22 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
'''

class Solution:
    def isHappy(self, n: int) -> bool:
        if n <= 0:
            return False
        visited = set()
        while True:
            _sum = 0
            while n:
                _sum += (n % 10) ** 2
                n //= 10
            # print(_sum)
            if _sum == 1:
                return True
            elif _sum in visited:
                return False
            visited.add(_sum)
            n = _sum

    def isHappy(self, n: int) -> bool:
        # Use fast and slow pointers
        if n<=0:
            return False
        def sum_of_squares(n):
            _sum = 0
            while n:
                _sum += (n % 10) ** 2
                n //= 10
            return _sum
        
        slow, fast = n, n
        while True:
            if slow == fast:
                return False
            if slow == 1:
                return True
            slow = sum_of_squares(slow)
            fast = sum_of_squares(fast)
            fast = sum_of_squares(fast)
            

print(Solution().isHappy(19))