#
# 两个字符串是否相等
# @param str1 string字符串 第一个字符串
# @param str2 string字符串 第二个字符串
# @return bool布尔型
#
class Solution:
    def __init__(self):
        self.mem = {}

    def isStrsEqu(self , str1 , str2 ):
        # write code here
        if((str1, str2) in self.mem):
            return self.mem[(str1, str2)]
        str_len = len(str1)
        if(str_len==1):
            if str1==str2:
                self.mem[(str1, str2)] = True
            else:
                self.mem[(str1, str2)] = False
            return self.mem[(str1, str2)]
        
        substr11 = str1[:str_len//2]
        substr12 = str1[str_len//2:]
        substr21 = str2[:str_len//2]
        substr22 = str2[str_len//2:]
        if (self.isStrsEqu(substr11, substr21) and self.isStrsEqu(substr12, substr22)) or (self.isStrsEqu(substr11, substr22) and self.isStrsEqu(substr12, substr21)):
            self.mem[(str1, str2)] = True
        else:
            self.mem[(str1, str2)] = False
        return self.mem[(str1, str2)]

if __name__ =='__main__':
    print(Solution().isStrsEqu("aaba", "abaa"))