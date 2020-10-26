/*
Given a collection of distinct integers, 
return all possible permutations.

Example:
Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
*/
#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

class Solution {
private:
    vector<vector<int>> ans;
public:
    vector<vector<int>> permute(vector<int>& nums) {
        unordered_set<int> visited;
        vector<int> path;
        backtrack(nums, visited, path);
        return ans;
    }
    
    void backtrack(vector<int>& nums, unordered_set<int>& visited, vector<int> path){
        if(path.size()==nums.size()){
            ans.push_back(path);
        }
        for(auto n : nums){
            if(visited.find(n)==visited.end()){
                path.push_back(n);
                visited.insert(n);
                backtrack(nums, visited, path);
                path.pop_back();
                visited.erase(n);
            }
        }
    }
};