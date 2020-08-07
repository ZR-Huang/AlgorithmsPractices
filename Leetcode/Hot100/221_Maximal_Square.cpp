/*
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing 
only 1's and return its area.

Example:
Input: 
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Output: 4
*/
#include <vector>
#include <string.h>
using namespace std;

class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        int m = matrix.size();
        if(m == 0) return 0;
        int n = matrix[0].size();
        int maxSide = 0;
        int dp[m][n];
        memset(dp, 0, sizeof(int)*m*n);
        for(int i=0; i<m; i++)
            for(int j=0; j<n; j++){
                if(matrix[i][j]=='1'){
                    dp[i][j] = j==0 ? 1 : dp[i][j-1]+1;
                    int width = dp[i][j];
                    for(int k = i; k>i-width && k>=0; k--){
                        if(dp[k][j]==0) break;
                        width = min(width, dp[k][j]);
                        maxSide = max(maxSide, min(width, i-k+1));
                    }
                    
                }
            }
        return maxSide *maxSide;
    }

    int maximalSquare(vector<vector<char>>& matrix) {
        int m = matrix.size();
        if(m==0) return 0;
        int n = matrix[0].size();
        int dp[m+1][n+1];
        memset(dp, 0, sizeof(int)*(m+1)*(n+1));
        int maxSide = 0;
        for (int i=1; i<=m; i++)
            for (int j=1; j<=n ;j++)
                if(matrix[i-1][j-1]=='1'){
                    dp[i][j] = min(min(dp[i-1][j], dp[i][j-1]), dp[i-1][j-1])+1;
                    maxSide = max(maxSide, dp[i][j]);
                }
        return maxSide * maxSide;
    }
};