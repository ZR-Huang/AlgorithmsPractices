/*
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
*/
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int search(vector<int>& nums, int target) {
        if(nums.size()==0) return -1;
        int pivot_index = find_maximum(nums);
        int res = binary_search(nums, 0, pivot_index, target);
        if (res==-1) res = binary_search(nums, pivot_index+1, nums.size()-1, target);
        return res;
    }

    int find_maximum(vector<int>& nums){
        int l = 0, r = nums.size()-1;
        int maximum = nums[0];
        while (l <= r)
        {
            int mid = (l+r) / 2;
            if(nums[mid] < maximum) r = mid - 1;
            else{
                l = mid + 1;
                maximum = nums[mid];
            }
        }
        return l-1;
    }

    int binary_search(vector<int>& nums, int start, int end, int target){
        while (start <= end)
        {
            int mid = (start+end) / 2;
            if(nums[mid] < target) start = mid+1;
            else if(nums[mid] > target) end = mid-1;
            else return mid;
        }
        return -1;
    }
};

int main(){
    vector<int> nums = {4,5,6,7,0,1,2};
    Solution s;
    cout<<s.search(nums, 3)<<endl;
    return 0;
}