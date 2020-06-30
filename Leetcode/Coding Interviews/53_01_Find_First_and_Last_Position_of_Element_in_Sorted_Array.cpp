/*
注意：本题与主站 34 题相同（仅返回值不同）：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/


统计一个数字在排序数组中出现的次数。

示例 1:
输入: nums = [5,7,7,8,8,10], target = 8
输出: 2

示例 2:
输入: nums = [5,7,7,8,8,10], target = 6
输出: 0
 
限制：
0 <= 数组长度 <= 50000
*/
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    int search(vector<int>& nums, int target) {
        unordered_map<int, int> count;
        for(auto n : nums){
            if(count.count(n)==0) count[n]=1;
            else count[n]++;
        }
        return count[target];
    }

    int search_v2(vector<int>& nums, int target) {
        // binary search
        int left = 0, right = nums.size()-1;
        int target_pos = -1;
        while(left <= right){
            int mid = (left+right) / 2;
            if(nums[mid] < target){
                left = mid + 1;
            } else if (nums[mid] > target) {
                right = mid-1;
            } else {
                target_pos = mid;
                break;
            }
        }
        int count = 0;
        for(int i=target_pos; i<nums.size() && nums[i]==target; i++)
            count++;
        for(int i=target_pos-1; i>=0 && nums[i]==target; i--)
            count++;
        return count;
    }

    int search_v3(vector<int>& nums, int target) {
        return helper(nums, target)-helper(nums, target-1);
    }

    int helper(vector<int>& nums, int target) {
        int i = 0, j = nums.size()-1;
        while(i <= j){
            int m = (i + j) / 2;
            if(nums[m] <= target) i = m + 1;
            else j = m - 1;
        }
        return i;
    }
};

int main(){
    vector<int> nums = {5,7,7,8,8,10};
    Solution s;
    s.search_v2(nums, 8);
    return 0;
}