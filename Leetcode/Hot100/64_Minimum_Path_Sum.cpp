/*
Given a m x n grid filled with non-negative numbers, 
find a path from top left to bottom right which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.

Example:
Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
*/
#include <bits/stdc++.h>
#include <iostream>
#include <vector>
#include <set>
using namespace std;

class Solution {
private:
    vector<vector<int>> grid;
    set<pair<int, int>> visited;
    int m, n, minAns;
public:
    int minPathSum(vector<vector<int>>& grid) {
        this->grid = grid;
        m = grid.size();
        n = grid[0].size();
        minAns = INT_MAX;
        DFS(0, 0, 0);
        return minAns;
    }

    void DFS(int i, int j, int sum){
        if (i == m-1 && j == n-1) {// reach the right bottom
            minAns = min(minAns, sum + grid[i][j]);
            return ;
        }
        if (i+1 < m) {
            DFS(i+1, j, sum + grid[i][j]);
        }
        if (j+1 < n ) {
            DFS(i, j+1, sum + grid[i][j]);
        }
    }

    int DP(vector<vector<int>>& grid) {
        int dp[m][n];
        // initialize
        dp[0][0] = grid[0][0];
        for (int i=1; i<m; i++) dp[i][0] = grid[i][0] + dp[i-1][0];
        for (int j=1; j<n; j++) dp[0][j] = grid[0][j] + dp[0][j-1];

        for(int i=1; i<m; i++)
            for (int j=1; j<n; j++) 
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j];
        return dp[m-1][n-1];
    }
};
