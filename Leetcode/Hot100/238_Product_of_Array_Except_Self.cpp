/*
Given an array nums of n integers where n > 1,  return an array output such that output[i] 
is equal to the product of all the elements of nums except nums[i].

Example:
Input:  [1,2,3,4]
Output: [24,12,8,6]

Constraint: It's guaranteed that the product of the elements of any prefix or suffix 
of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
*/
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int length = nums.size();
        vector<int> left(length, 0), right(length, 0);
        vector<int> answer(length, 0);
        left[0] = right[length-1] = 1;
        for(int i=1; i<length; i++)
            left[i] = left[i-1]*nums[i-1];
        for(int i=length-2; i>=0; i--)
            right[i] = right[i+1]*nums[i+1];
        for(int i=0; i<length; i++)
            answer[i] = left[i]*right[i];
        return answer;
    }

    vector<int> productExceptSelf(vector<int>& nums) {
        int length = nums.size();
        vector<int> answer(length, 0);
        answer[0] = 1;
        for(int i=1; i<length; i++)
            answer[i] = answer[i-1]*nums[i-1];
        int right = 1;
        for(int i=length-1; i>=0; i--)
        {
            answer[i] = answer[i] * right;
            right = right * nums[i];
        }
        return answer;
    }
};