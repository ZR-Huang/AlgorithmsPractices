/*
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:
Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
*/
#include <vector>
#include <unordered_set>
using namespace std;

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> num_map;
        for(auto n : nums) num_map.insert(n);
        int ans = 0;
        
        for(const int& num : num_map) {
            if(!num_map.count(num-1)) { // 不存在前驱元素
                int currNum = num;
                int currLen = 1;
                while(num_map.count(currNum+1)) {
                    currNum++;
                    currLen++;
                }
                ans = max(ans, currLen);
            }
        }
        return ans;
    }
};