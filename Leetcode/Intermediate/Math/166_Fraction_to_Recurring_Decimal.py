'''
Given two integers representing the numerator and 
denominator of a fraction, return the fraction in string format.
If the fractional part is repeating, enclose the 
repeating part in parentheses.

Example 1:
Input: numerator = 1, denominator = 2
Output: "0.5"

Example 2:
Input: numerator = 2, denominator = 1
Output: "2"

Example 3:
Input: numerator = 2, denominator = 3
Output: "0.(6)"
'''

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        ans = ""
        if numerator % denominator == 0:
            return str(numerator // denominator)

        # sign process
        ans = "-"+ans if numerator < 0 or denominator < 0 else ans
        numerator = abs(numerator)
        denominator = abs(denominator)
        
        res = numerator // denominator
        ans += str(res)
        numerator = numerator % denominator

        hashmap = {}
        count = 0
        ans += "."
        while numerator not in hashmap and (numerator != 0):
            hashmap[numerator] = count
            numerator *= 10
            res = numerator // denominator
            numerator = numerator % denominator
            count += 1
            ans += str(res)
        if numerator != 0:
            start = hashmap[numerator]
            ans = ans.split(".")
            ans[1] = ans[1][:start] + "("+ans[1][start:] + ")"
            ans = ".".join(ans)
        return ans

print(Solution().fractionToDecimal(1, 19))
print(Solution().fractionToDecimal(3, 2))
print(Solution().fractionToDecimal(2, 1))
print(Solution().fractionToDecimal(5, 3))