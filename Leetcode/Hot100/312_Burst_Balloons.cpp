/*
Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:
You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100

Example:
Input: [3,1,5,8]
Output: 167 
Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
             coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
*/
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> val;
    vector<vector<int>> mem;
    int solve(int left, int right){
        if(left >= right-1) return 0;
        if(mem[left][right]!= -1) return mem[left][right];
        for(int i = left+1; i< right; i++){
            int sum = val[left]* val[i]*val[right];
            sum += solve(left, i) + solve(i, right);
            mem[left][right] = max(mem[left][right], sum);
        }
        return mem[left][right];
    }
    int maxCoins(vector<int>& nums) {
        int n = nums.size();
        val.resize(n+2);
        for(int i = 1; i <= n; i++)
            val[i] = nums[i-1];
        val[0] = val[n+1] = 1;
        mem.resize(n+2, vector<int>(n+2, -1));
        return solve(0, n+1);
    }
};