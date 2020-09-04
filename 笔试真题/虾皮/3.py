#
# 获取子串相乘的最大值
# @param str string字符串 输入的字符串
# @return int整型
#
class Solution:
    def getMaxMul(self , str ):
        # write code here
        ll, lr, rl, rr = 0, 1, len(str)-2, len(str)-1
        left = set(str[ll])
        right = set(str[rr])
        ans = (lr-ll)*(rr-rl)
        while lr < rl:
            if(left.add(str[lr]) and right.add(str[rl]))