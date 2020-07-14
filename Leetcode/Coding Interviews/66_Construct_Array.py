'''
给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，其中 B 中的元素 B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。不能使用除法。

示例:
输入: [1,2,3,4,5]
输出: [120,60,40,30,24]

提示：
所有元素乘积之和不会溢出 32 位整数
a.length <= 100000
'''

from typing import List

class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        n = len(a)
        b = []
        i, product = 0, 1
        while i<n:
            b.append(product)
            product *= a[i]
            i+=1
        i, product = n-1, 1
        while i>=0:
            b[i]*=product
            product*=a[i]
            i-=1
        return b

    def constructArr(self, a: List[int]) -> List[int]:
        b, tmp = [1]*len(a), 1
        for i in range(1, len(a)):
            b[i] = b[i-1]*a[i-1]
        for i in range(len(a)-2, -1, -1):
            tmp *= a[i+1]
            b[i] *= tmp
        return b