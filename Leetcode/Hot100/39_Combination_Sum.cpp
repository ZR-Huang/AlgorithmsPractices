/*
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sums to target.
The same repeated number may be chosen from candidates unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]

Example 2:
Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

Constraints:
1 <= candidates.length <= 30
1 <= candidates[i] <= 200
Each element of candidate is unique.
1 <= target <= 500
*/
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
private:
    vector<int> candidates;
    vector<vector<int>> res;
    vector<int> path;
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        this->candidates = candidates;
        backtrack(0, target);
        return res;
    }

    void backtrack(int start, int target) {
        if (target == 0){
            res.push_back(path);
            return ;
        }
        for (int i = start; i < candidates.size() && target - candidates[i]>=0; i++){
            path.push_back(candidates[i]);
            backtrack(i, target - candidates[i]);
            path.pop_back();
        }
    }
};

int main() {
    vector<int> candidates = {2,3,6,7};
    int target = 7;
    Solution sol;
    vector<vector<int>> res = sol.combinationSum(candidates, target);
    return 0;
}