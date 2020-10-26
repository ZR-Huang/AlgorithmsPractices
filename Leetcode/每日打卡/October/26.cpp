/*
1365. How Many Numbers Are Smaller Than the Current Number

Given the array nums, for each nums[i] find out how many numbers in 
the array are smaller than it. That is, for each nums[i] you have to 
count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.
 
Example 1:
Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation: 
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1). 
For nums[3]=2 there exist one smaller number than it (1). 
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).

Example 2:
Input: nums = [6,5,4,8]
Output: [2,1,0,3]

Example 3:
Input: nums = [7,7,7,7]
Output: [0,0,0,0]

Constraints:
	2 <= nums.length <= 500
	0 <= nums[i] <= 100
*/

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        int len = nums.size();
        vector<int> ans (len, 0);
        for (int i = 0; i < len; i++){
            for (int j = 0; j < len; j++){
                if (i == j) continue;
                else if (nums[j] < nums[i]) ans[i]++;
            }
        }
        return ans;
    }

    vector<int> sortAndHash(vector<int>& nums) {
        vector<pair<int, int>> data;
        for(int i = 0; i < nums.size(); i++){
            data.emplace_back(nums[i], i);
        }

        sort(data.begin(), data.end());
        vector<int> ans(nums.size(), 0);
        int prev = -1;
        for(int i = 0; i < nums.size(); i++) {
            if (prev == -1 || data[i].first != data[i-1].first){
                prev = i;
            }
            ans[data[i].second] = prev;
        }
        return ans;
    }
};