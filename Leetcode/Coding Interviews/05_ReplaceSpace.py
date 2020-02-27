'''
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

示例 1：
输入：s = "We are happy."
输出："We%20are%20happy."

限制：
0 <= s 的长度 <= 10000
'''
class Solution:
    def replaceSpace(self, s: str) -> str:
        """
        list(s) : O(N), the length of the string is donated as N.
        iterate the string : O(N)
        list assignment: O(1)
        join() : O(N)
        Total: O(N) 
        """
        if not s:
            return ''
        s_list = list(s)
        for i in range(len(s)):
            if s_list[i] == " ":
                s_list[i] = "%20"
        return ''.join(s_list)


"""
However, the similar methed implemented by C++ has the O(N**2) of time 
complexity.
When we meet a space in the string, we have to move the rest characters 
back. Therefore, there are the duplicated operations.
Next, we show the algorithm with the O(N) complexity in C++.
"""
"""
void ReplaceBlank(char string[], int length)
{
    // the length is the total size of the string array
    if(string == nullptr || length <=0)
        return;
    
    /* the length of string is donated as originalLength */
    int originalLength = 0;
    int numberOfBlank = 0;
    int i = 0;
    while(string[i]!='\0')
    {
        ++originalLength;
        if(string[i]=='')
            ++numberOfBlank;
        ++i;
    }
    /* the length of the new string is donated as newLength */
    int newLength = originalLength + numberOfBlank *2;
    if(newLength>length)
        return;
    
    int indexOfOriginal = originalLength;
    int indexOfNew = newLength;
    while(indexOfOriginal>=0 && indexOfNew > indexOfOriginal)
    {
        if(string[indexOfOriginal]=='')
        {
            string[indexOfNew--]='0';
            string[indexOfNew--]='2';
            string[indexOfNew--]='%';
        }
        else
        {
            string[indexOfNew--] = string[indexOfOriginal];
        }
        --indexOfOriginal;
    }
}
"""
        