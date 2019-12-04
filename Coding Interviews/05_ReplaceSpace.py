class Solution:
    def replaceSpace(self, s):
        """
        According to the time complexity of the basic operation of Python3,
        we analyze the complexity of our code.
        list(s) : O(N), the length of the string is donated as N.
        iterate the string : O(N)
        list assignment: O(1)
        join() : O(N)
        Total: O(N) 
        """
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
        