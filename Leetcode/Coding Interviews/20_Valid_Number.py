'''
注意：本题与主站 65 题相同：https://leetcode-cn.com/problems/valid-number/

请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，
字符串"+100"、"5e2"、"-123"、"3.1416"、"0123"及"-1E-16"都表示数值，(实际上该题的答案中"-1E-16"不是有效数值)
但"12e"、"1a3.14"、"1.2.3"、"+-5"及"12e+5.4"都不是。
'''
class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip() # 看评论区说有个测试用例为("1 ", True)
        if 'e' in s:
            parts = s.split('e')
            if len(parts)== 2 and ((self.checkInteger(parts[0]) or self.checkFloat(parts[0])) and self.checkInteger(parts[1])):
                return True
        else:
            if self.checkInteger(s) or self.checkFloat(s):
                return True
        return False

    def checkInteger(self, s, existSign=True):
        if not s:
            return False
        if existSign:
            if s[0] == '+' or s[0] == '-':
                s = s[1:]
        if not s: # 仅含正负号
            return False
        for c in s:
            if not c.isdigit():
                return False
        return True

    def checkFloat(self, s, existSign=True):
        if not s:
            return False
        if existSign:
            if s[0] == '+' or s[0] == '-':
                s = s[1:]
        if not s: # 仅含正负号
            return False
        parts = s.split('.')
        if len(parts) == 2:
            if not parts[0] and self.checkInteger(parts[1], existSign=False):
                return True
            elif not parts[1] and self.checkInteger(parts[0], existSign=False):
                return True
            elif self.checkInteger(parts[0], existSign=False) and self.checkInteger(parts[1], existSign=False):
                return True
        else:
            return False
        