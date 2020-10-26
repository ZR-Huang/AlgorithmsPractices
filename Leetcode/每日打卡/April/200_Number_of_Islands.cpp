/*
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input:
11110
11010
11000
00000
Output: 1

Example 2:
Input:
11000
11000
00100
00011
Output: 3
*/
#include <iostream>
#include <vector>
#include <queue>
#include <utility>
using namespace std;

class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int num_islands = 0;
        if (grid.size()==0) return num_islands;
        int m = grid.size(), n = grid[0].size();
        queue<pair<int, int>> q;
        for (int i=0; i<m; i++){
            for (int j=0; j<n; j++){
                if (grid[i][j]=='1') {
                    num_islands++;
                    q.push({i, j});
                    grid[i][j] = '0';
                    while(!q.empty()){
                        auto [i, j] = q.front();
                        q.pop();
                        if (i-1>=0 && grid[i-1][j]=='1') q.push({i-1,j}), grid[i-1][j]='0';
                        if (i+1<m && grid[i+1][j]=='1') q.push({i+1,j}), grid[i+1][j]='0';
                        if (j-1>=0 && grid[i][j-1]=='1') q.push({i, j-1}), grid[i][j-1]='0';
                        if (j+1<n && grid[i][j+1]=='1') q.push({i, j+1}), grid[i][j+1]='0';
                    }
                }
            }
        }
        return num_islands;
    }
};

int main(){
    vector<vector<char>> grid = {{'1','1','1','1','0'},{'1','1','0','1','0'},{'1','1','0','0','0'},{'0','0','0','0','0'}};
    Solution s;
    int ans = s.numIslands(grid);
    return 0;
}