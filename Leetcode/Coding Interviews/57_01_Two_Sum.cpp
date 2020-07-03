/*
输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。 

示例 1：
输入：nums = [2,7,11,15], target = 9
输出：[2,7] 或者 [7,2]

示例 2：
输入：nums = [10,26,30,31,47,60], target = 40
输出：[10,30] 或者 [30,10]

限制：
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^6
*/

#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> res = {0, 0};
        unordered_map<int, int> map;
        for(int num : nums){
            if(map.count(num)==0){
                map[target-num] = num;
            } else {
                res[0] = map[num];
                res[1] = num;
                break;
            }
        }
        return res;
    }

    vector<int> twoSum_v2(vector<int>& nums, int target) {
        // double pointer
        vector<int> res ;
        int i = 0 , j = nums.size() - 1;
        while(i < j){
            if(nums[i]+nums[j] > target) j--;
            else if(nums[i]+nums[j] < target) i++;
            else{
                res.push_back(nums[i]);
                res.push_back(nums[j]);
                break;
            }
        }
        return res;
    }
};