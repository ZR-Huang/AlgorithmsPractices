/*
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:
Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.

Example 2:
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
*/
#include <climits>
#include <unordered_map>
#include <vector>
#include <unordered_set>
#include <cmath>
using namespace std;

class Solution {
public:
    int numSquares(int n) {
        vector<int> squareNum;
        vector<int> dp(n+1, INT_MAX);
        dp[0] = 0;
        for(int i = 1; i <= (int)sqrt(n); i++)
            squareNum.push_back(i*i);
        for(int i = 1; i <= n; i++){
            for(auto square : squareNum)
            {
                if(i < square) break;
                dp[i] = min(dp[i], dp[i-square]+1);
            }
        }
        return dp[n];
    }

    int numSquares(int n) {
        // BFS + greedy
        vector<int> squareNums;
        unordered_set<int> queue;
        int level = 0;
        for(int i = 1; i <= (int)sqrt(n); i++)
            squareNums.push_back(i*i);
        queue.insert(n);
        while(!queue.empty()){
            level++;
            unordered_set<int> next_q;
            for(auto remain : queue){
                for(auto square: squareNums){
                    if(remain == square) return level;
                    else if(remain < square) break;
                    else next_q.insert(remain-square);
                }
            }
            queue = next_q;
        }
        return level;
    }

};
