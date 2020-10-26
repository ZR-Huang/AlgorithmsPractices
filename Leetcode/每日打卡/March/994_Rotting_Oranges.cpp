/*
In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  
If this is impossible, return -1 instead.

Example 1:
Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:
Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:
Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
 
Note:
1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] is only 0, 1, or 2.
*/
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        vector<pair<int, int>> rot_list;
        for(int i=0; i<m; i++)
            for(int j=0; j<n; j++)
                if(grid[i][j]==2) rot_list.push_back({i, j});
        
        int time = 0;
        while (!rot_list.empty())
        {
            vector<pair<int, int>> new_rot_list;
            for (auto p : rot_list)
            {
                if(p.first-1>=0 && grid[p.first-1][p.second]==1) {
                    grid[p.first-1][p.second] = 2;
                    new_rot_list.push_back({p.first-1, p.second});
                }
                if(p.first+1<m && grid[p.first+1][p.second]==1) {
                    grid[p.first+1][p.second] = 2;
                    new_rot_list.push_back({p.first+1, p.second});
                }
                if(p.second-1>=0 && grid[p.first][p.second-1]==1) {
                    grid[p.first][p.second-1] = 2;
                    new_rot_list.push_back({p.first, p.second-1});
                }
                if(p.second+1<n && grid[p.first][p.second+1]==1) {
                    grid[p.first][p.second+1] = 2;
                    new_rot_list.push_back({p.first, p.second+1});
                }
            }
            if (new_rot_list.empty()) break;
            rot_list = new_rot_list;
            time++;
        }
        for(int i=0; i<m; i++)
            for(int j=0; j<n; j++)
                if(grid[i][j]==1) return -1;
        return time;
    }
};