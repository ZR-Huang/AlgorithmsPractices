/*
输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。

示例 1:
输入: [10,2]
输出: "102"

示例 2:
输入: [3,30,34,5,9]
输出: "3033459"

提示:
0 < nums.length <= 100
说明:
输出结果可能非常大，所以你需要返回一个字符串而不是整数
拼接起来的数字可能会有前导 0，最后结果不需要去掉前导 0
*/
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    string minNumber(vector<int>& nums) {
        vector<int> sorted_nums = mergeSort(nums, 0, nums.size()-1);
        string res;
        for(auto i : sorted_nums){
            res += to_string(i);
        }
        return res;
    }

    vector<int> mergeSort(vector<int>& nums, int l, int r){
        if(l == r){
            return vector<int> {nums[l]};
        }
        int mid = (l+r) / 2;
        vector<int> left = mergeSort(nums, l, mid);
        vector<int> right = mergeSort(nums, mid+1, r);
        vector<int> res = merge(left, right);
        return res;
    }

    vector<int> merge(vector<int>& left, vector<int>& right){
        vector<int> tmp;
        int i=0, j=0;
        while(i<left.size() && j<right.size()){
            if(lessEqual(left[i], right[j])){
                tmp.push_back(left[i]);
                i++;
            } else {
                tmp.push_back(right[j]);
                j++;
            }
        }
        for(;i<left.size();i++)
            tmp.push_back(left[i]);
        for(;j<right.size();j++)
            tmp.push_back(right[j]);
        return tmp;
    }

    bool lessEqual(int a, int b){
        if(a==b) return true;
        string aStr = to_string(a);
        string bStr = to_string(b);
        long a_concat_b = stol(aStr+bStr);
        long b_concat_a = stol(bStr+aStr);
        return a_concat_b < b_concat_a;
    }
};