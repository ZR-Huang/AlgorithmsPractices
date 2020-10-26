/*
一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。
要求时间复杂度是O(n)，空间复杂度是O(1)。


示例 1：
输入：nums = [4,1,4,6]
输出：[1,6] 或 [6,1]

示例 2：
输入：nums = [1,2,10,4,1,4,3,3]
输出：[2,10] 或 [10,2]

限制：
    2 <= nums <= 10000
*/
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> singleNumbers(vector<int>& nums) {
        // https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof/solution/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-by-leetcode/
        vector<int> ans = {0, 0};
        int sum = 0;
        for(int num: nums)
            sum ^= num;
        int flag = 1;
        while((flag & sum) == 0)
            flag <<= 1;
        for(int num: nums)
            if(num & flag)
                ans[0] ^= num;
            else
                ans[1] ^= num;
        return ans;
    }
};