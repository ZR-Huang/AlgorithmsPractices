/*
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) 
which has the largest product.

Example 1:
Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
*/
#include <vector>
using namespace std;

class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int maxF[nums.size()], minF[nums.size()], max_prod;
        maxF[0] = minF[0] = max_prod = nums[0];
        for(int i = 1; i < nums.size(); i++) {
            maxF[i] = max(maxF[i-1]*nums[i], max(nums[i], nums[i]*minF[i-1]));
            minF[i] = min(maxF[i-1]*nums[i], min(nums[i], nums[i]*minF[i-1]));
            max_prod = max(max_prod, maxF[i]);
        }
        return max_prod;
    }

    int maxProduct(vector<int>& nums) {
        // 压缩空间
        int maxF = nums[0], minF=nums[0], max_prod = nums[0];
        for(int i = 1; i < nums.size(); i++){
            int mx = maxF, mn = minF;
            maxF = max(mx*nums[i], max(nums[i], nums[i]*mn));
            minF = min(mx*nums[i], min(nums[i], nums[i]*mn));
            max_prod = max(max_prod, maxF);
        }
        return max_prod;
    }
};