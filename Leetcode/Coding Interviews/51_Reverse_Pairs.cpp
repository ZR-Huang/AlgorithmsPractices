/*
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组，求出这个数组中的逆序对的总数。

示例 1:
输入: [7,5,6,4]
输出: 5

限制：
0 <= 数组长度 <= 50000
*/
#include <iostream>
#include <vector>
using namespace std;

class Solution {
private:
    int reverse_pairs = 0;
public:
    int reversePairs(vector<int>& nums) {
        mergeSort(nums, 0, nums.size()-1);
        return reverse_pairs;
    }

    vector<int> mergeSort(vector<int>& nums, int start, int end) {
        vector<int> ans;
        if(start == end){
            ans.push_back(nums[start]);
            return ans;
        }
        int mid = (start+end) / 2;
        vector<int> left = mergeSort(nums, start, mid);
        vector<int> right = mergeSort(nums, mid+1, end);

        int i=0, j=0;
        while(i<left.size() && j<right.size()){
            if(left[i] <= right[j]) {
                ans.push_back(left[i]);
                i++;
                reverse_pairs+= j;
            }
            else{
                ans.push_back(right[j]);
                j++;
            }
        }
        for (; i<left.size(); i++){
            ans.push_back(left[i]);
            reverse_pairs += j;
        }
        for (; j<right.size(); j++)
            ans.push_back(right[j]);
        return ans;
    }
};

int main(){
    vector<int> nums = {1, 2, 3, 4};
    Solution s;
    int ans = s.reversePairs(nums);
    return 0;
}