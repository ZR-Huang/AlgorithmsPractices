/*
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) 
connected 4-directionally (horizontal or vertical.) You may assume all four edges 
of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. 
(If there is no island, the maximum area is 0.)

Example 1:
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.

Example 2:
[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.

Note: The length of each dimension in the given grid does not exceed 50.
*/
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        int max_area = 0;
        for(int i=0; i<m; i++)
            for(int j=0; j<n; j++)
                if(grid[i][j]) max_area = max(max_area, getAreaOfIsland(grid, i, j, m, n));
        return max_area;
    }

    int getAreaOfIsland(vector<vector<int>>& grid, int i, int j, int m, int n) {
        queue<pair<int, int>> q;
        q.push({i,j});
        int area = 0;
        while (q.empty())
        {
            pair<int, int> p = q.front();
            q.pop();
            // grid[p.first][p.second] = 0;
            area++;
            if(p.first-1>=0 && grid[p.first-1][p.second]==1) {
                grid[p.first-1][p.second] = 0;
                q.push({p.first-1, p.second});
            }
            if(p.first+1<m && grid[p.first+1][p.second]==1) {
                grid[p.first+1][p.second] = 0;
                q.push({p.first+1, p.second});
            }
            if(p.second-1>=0 && grid[p.first][p.second-1]==1) {
                grid[p.first][p.second-1] = 0;
                q.push({p.first, p.second-1});
            }
            if(p.second+1<n && grid[p.first][p.second+1]==1) {
                grid[p.first][p.second+1] = 0;
                q.push({p.first, p.second+1});
            }
        }
        return area;
    }
};