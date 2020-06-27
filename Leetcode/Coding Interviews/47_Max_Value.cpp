/*
在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。
你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。
给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？ 

示例 1:
输入: 
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 12
解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物

提示：
0 < grid.length <= 200
0 < grid[0].length <= 200
*/
#include <iostream>
#include <vector>
using namespace std;

class Solution {
private:
    int max_value = 0;
public:
    int maxValue(vector<vector<int>>& grid) {
        return dynamicProgramming(grid);
    }

    void dfs(vector<vector<int>> &grid, int x, int y, int value){
        if(x==grid.size()-1 && y==grid[0].size()-1){
            max_value = max(max_value, value+grid[x][y]);
        }
        if(x+1<grid.size()){
            dfs(grid, x+1, y, value+grid[x][y]);
        }
        if(y+1<grid[0].size()){
            dfs(grid, x, y+1, value+grid[x][y]);
        }
    }

    int dynamicProgramming(vector<vector<int>>& grid) {
        int dp[grid.size()+1][grid[0].size()+1];
        for (int i = 0; i <= grid.size(); i++)
            dp[i][0] = 0;
        for (int i = 0; i <= grid[0].size(); i++)
            dp[0][i] = 0;
        for (int i = 1; i <= grid.size(); i++){
            for(int j = 1; j<= grid[0].size(); j++) {
                dp[i][j] = max(dp[i][j-1], dp[i-1][j]) + grid[i-1][j-1];
            }
        }
        return dp[grid.size()][grid[0].size()];
    }
};