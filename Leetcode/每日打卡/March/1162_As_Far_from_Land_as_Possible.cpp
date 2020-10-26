/*
Given an N x N grid containing only values 0 and 1, where 0 represents water and 1 represents land, 
find a water cell such that its distance to the nearest land cell is maximized and return the distance.
The distance used in this problem is the Manhattan distance: 
the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

If no land or water exists in the grid, return -1.

Example 1:
Input: [[1,0,1],[0,0,0],[1,0,1]]
Output: 2
Explanation: 
The cell (1, 1) is as far as possible from all the land with distance 2.

Example 2:
Input: [[1,0,0],[0,0,0],[0,0,0]]
Output: 4
Explanation: 
The cell (2, 2) is as far as possible from all the land with distance 4.
 
Note:
- 1 <= grid.length == grid[0].length <= 100
- grid[i][j] is 0 or 1
*/
#include <iostream>
#include <vector>
#include <queue>
#include <set>
using namespace std;

class Solution {
public:
    int maxDistance(vector<vector<int>>& grid) {
        queue<pair<int, int>> q;
        int N = grid.size();
        for(int i=0; i<N; i++)
            for(int j=0; j<N; j++)
                if(grid[i][j]) q.push({i, j});
        if(q.empty()) return -1;

        int distance = 0;
        int dx[] = {-1,1,0,0};
        int dy[] = {0,0,-1,1};
        bool hasOcean = false;
        while(!q.empty()){
            int size = q.size();
            while(size--){
                pair<int, int> p = q.front();
                q.pop();
                for(int i=0; i<4; i++){
                    if(p.first+dx[i]<0 || p.first+dx[i]>=N || p.second+dy[i]<0 || p.second+dy[i]>=N || grid[p.first+dx[i]][p.second+dy[i]] == 1)
                        continue;
                    q.push({p.first+dx[i], p.second+dy[i]});
                    hasOcean = true;
                    grid[p.first+dx[i]][p.second+dy[i]] = 1;
                }
            }
            distance++;
        }
        if(!hasOcean) return -1;
        return distance-1;
    }
};