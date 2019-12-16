'''
1292. Maximum Side Length of a Square with Sum Less than or Equal to Threshold
This problem can be solved by the prefix sum algorithm,
but the code in python will exceed the time limitation.

This implemented code is just presented as the template of the 
prefix sum algorithm
'''
class Solution:
    def maxSideLength(self, mat, threshold: int) -> int:
        '''
        Adopt the prefix sum algorithm
        '''
        m, n = len(mat), len(mat[0])
        _sum = [[0]* (n+1) for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                _sum[i][j] = _sum[i-1][j] + _sum[i][j-1] - _sum[i-1][j-1] + mat[i-1][j-1]

        ans = 0

        for k in range(1, min(m,n)+1):
            for i in range(1, m+1):
                for j in range(1, n+1):
                    if i-k < 0 or j-k < 0:
                        continue
                    tmp = _sum[i][j] - _sum[i-k][j] - _sum[i][j-k] + _sum[i-k][j-k]
                    if tmp <= threshold:
                        ans = max(ans, k)
        
        return ans