/*
注意：本题与主站 233 题相同：https://leetcode-cn.com/problems/number-of-digit-one/

输入一个整数 n ，求1～n这n个整数的十进制表示中1出现的次数。
例如，输入12，1～12这些整数中包含1 的数字有1、10、11和12，1一共出现了5次。

示例 1：
输入：n = 12
输出：5

示例 2：
输入：n = 13
输出：6

限制：
    1 <= n < 2^31
*/
#include <iostream>
#include <stack>
#include <math.h>

using namespace std;

class Solution {
public:
    /* int countDigitOne(int n) {
        int count = 0;
        for (int i=1; i<=n; i++){
            int tmp = i;
            while(tmp!=0){
                count += (tmp % 10 == 1 ? 1 : 0);
                tmp /= 10;
            }
        }
        return count;
    } */

    int countDigitOne(int n) {
        int x = n;
        stack<int> s;
        do{
            s.push(x%10);
            x /= 10;
        }while(x!=0);
        int length = s.size();
        int arr[length];
        for (int i = 0; i< length; i++)
        {
            arr[i] = s.top();
            s.pop();
        }
        int sum_of_one = 0;
        int pre_num = 0;
        int post_num = 0;
        for(int i=1; i<length; i++)
            post_num = post_num * 10 + arr[i];
        for(int i=0; i<length; i++){
            if(arr[i] > 1){
                sum_of_one += (pre_num + 1) * (int)pow(10, length-1-i);
            }else if (arr[i] == 1) {
                sum_of_one += (pre_num * (int)pow(10, length-1-i) + post_num + 1);
            }else{
                sum_of_one += (pre_num * (int)pow(10, length-1-i));
            }
            if(i < length-1){
                pre_num = pre_num * 10 + arr[i];
                post_num = post_num - arr[i+1] * (int)pow(10, length-2-i);
            }
        }
        return sum_of_one;
    }
};

int main(){
    Solution s;
    s.countDigitOne(0);
    return 0;
}