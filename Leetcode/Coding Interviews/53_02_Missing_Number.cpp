/*
一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。
在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。 

示例 1:
输入: [0,1,3]
输出: 2

示例 2:
输入: [0,1,2,3,4,5,6,7,9]
输出: 8
 
限制：
1 <= 数组长度 <= 10000
*/

#include <vector>
using namespace std;

class Solution {
public:
    int missingNumber(vector<int>& nums) {
        size_t i = 0;
        for (; i < nums.size(); i++)
        {
            if(nums[i] != i) return i;
        }
        return i;
    }

    int missingNumber(vector<int>& nums) {
        // binary search
        int i = 0, j = nums.size()-1;
        while(i <= j) {
            int m = (i + j) / 2;
            if(nums[m] > m) j = m - 1;
            else i = m + 1;
        }
        return i - 1;
    }
};