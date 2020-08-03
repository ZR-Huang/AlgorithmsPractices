/*
Given a non-empty binary tree, find the maximum path sum.
For this problem, a path is defined as any sequence of nodes from some starting node 
to any node in the tree along the parent-child connections. The path must contain at least one node 
and does not need to go through the root.

Example 1:
Input: [1,2,3]
       1
      / \
     2   3
Output: 6

Example 2:
Input: [-10,9,20,null,null,15,7]
   -10
   / \
  9  20
    /  \
   15   7
Output: 42
*/

#include <iostream>
#include <climits>
using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    int maxAns = INT_MIN;
    int maxPathSum(TreeNode* root) {
        int res = maxGain(root);
        return maxAns;
    }

    int maxGain(TreeNode* root) {
        if(!root) return 0;
        int leftGain = max(maxGain(root->left), 0);
        int rightGain = max(maxGain(root->right), 0);
        int gain = leftGain + rightGain + root->val;
        maxAns = max(maxAns, gain);
        return root->val + max(leftGain, rightGain);
    }
};