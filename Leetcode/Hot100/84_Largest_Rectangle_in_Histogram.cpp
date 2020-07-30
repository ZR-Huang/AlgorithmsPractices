/*
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, 
find the area of largest rectangle in the histogram.

Example:
Input: [2,1,5,6,2,3]
Output: 10
*/
#include <vector>
#include <stack>
using namespace std;

class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        // 暴力解法
        int n = heights.size(), maxAns = 0;
        if (n == 0) return maxAns;
        int dp[n][n];
        for (int i=0; i<n; i++) {
            int minH = heights[i];
            for (int j=i; j<n; j++){
                minH = min(minH, heights[j]);
                dp[i][j] = (j-i+1)*minH;
                maxAns = max(maxAns, dp[i][j]);
            }
        }
        return maxAns;
    }

    int useStack(vector<int>& heights) {
        vector<int> left(heights.size()), right(heights.size());
        stack<int> s;
        for (int i = 0; i < heights.size(); i++){
            while (!s.empty() && heights[s.top()] >= heights[i]){
                s.pop();
            }
            left[i] = (s.empty() ? -1 : s.top());
            s.push(i);
        }
        s = stack<int>();
        for (int i = heights.size()-1; i>= 0; i--) {
            while(!s.empty() && heights[s.top()] >= heights[i]) {
                s.pop();
            }
            right[i] = (s.empty() ? heights.size() : s.top());
            s.push(i);
        }
        int maxAns = 0;
        for (int i = 0; i < heights.size(); i++) {
            maxAns = max(heights[i]*(right[i]-left[i]-1), maxAns);
        }
        return maxAns;
    }
};