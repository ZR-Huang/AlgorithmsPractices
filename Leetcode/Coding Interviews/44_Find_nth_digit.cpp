/*
注意：本题与主站 400 题相同：https://leetcode-cn.com/problems/nth-digit/

数字以0123456789101112131415…的格式序列化到一个字符序列中。
在这个序列中，第5位（从下标0开始计数）是5，第13位是1，第19位是4，等等。
请写一个函数，求任意第n位对应的数字。

示例 1：
输入：n = 3
输出：3

示例 2：
输入：n = 11
输出：0
 
限制：
0 <= n < 2^31
*/
#include <iostream>
using namespace std;

class Solution {
public:
    int findNthDigit(int n) {
        if(n==0) return 0;
        int strLen = 0;
        for(int i = 1; ;i++){
            int res;
            string int_str = to_string(i);
            strLen += int_str.length();
            if(strLen>=n) {
                res = int_str[int_str.length()-1-(strLen-n)] - '0';
                return res;
            }
        }
    }

    int findNthDigit_v2(int n) {
        long digit = 1, start = 1;
        long count = 9;
        // 确定n所在的数字的位数
        while (n > count){
            n -= count;
            start *= 10;
            digit += 1;
            count = digit * start * 9;
        }
        //确定n所在的数字
        int num = start + (n-1)/digit;
        //确定所在数位在num的哪一位
        string s = to_string(num);
        int res = s[(n-1)%digit] - '0';
        return res;
    }
};