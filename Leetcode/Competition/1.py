class Solution:
    def generateTheString(self, n: int) -> str:
        if n & 1 == 0:
            ans = ''.join(['a'*(n-1),'b'])

        else:
            ans = 'a'*n
        return ans
            
print(Solution().generateTheString(7))