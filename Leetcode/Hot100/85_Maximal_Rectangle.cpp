/*
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example:
Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6
*/

#include <vector>
#include <stack>
#include <string.h>
using namespace std;

class Solution {
public:
    int maximalRectangle(vector<vector<char>>& matrix) {
        int m = matrix.size();
        if(m==0) return 0;
        int n = matrix[0].size();
        int maxArea = 0;
        int dp[m][n];
        memset(dp, 0, sizeof(int)*m*n);
        for(int i = 0; i < m; i++){
            for(int j = 0; j<n; j++) {
                if(matrix[i][j] == '1'){
                    dp[i][j] = j==0 ? 1 : dp[i][j-1]+1;
                    int width = dp[i][j];

                    for(int k = i; k>=0; k--){
                        width = min(width, dp[k][j]);
                        maxArea = max(width * (i-k+1), maxArea);
                    }
                }
            }
        }
        return maxArea;
    }
};