/*
给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。
一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

示例 1:
输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"

提示：
0 <= num < 2^31
*/
#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    int translateNum(int num) {
        string num_str = to_string(num);
        int dp[num_str.size()+1];
        dp[0] = 1, dp[1] = 1;
        for(int i=2; i<=num_str.size(); i++){
            if((num_str[i-2] == '1' && num_str[i-1]-'0' <=9 )|| (num_str[i-2] == '2' && num_str[i-1]-'0'<=5)){
                dp[i] = dp[i-1]+dp[i-2];
            } else {
                dp[i] = dp[i-1];
            }
        }
        return dp[num_str.size()];
    }

    int translateNum(int num) {
        // 「滚动数组」压缩空间
        string num_str = to_string(num);
        // int dp[num_str.size()+1];
        // dp[0] = 1, dp[1] = 1;
        int p = 0, q = 0, r = 1;
        for(int i=0; i<num_str.size(); i++){
            p = q;
            q = r;
            r = q;
            if (i==0) continue;
            auto pre = num_str.substr(i-1, 2);
            if(pre <= "25" && pre >= "10") {
                r = p + q;
            }
        }
        return r;
    }
};