/*
Given a binary tree, imagine yourself standing on the right side of it, 
return the values of the nodes you can see ordered from top to bottom.

Example:
Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
*/

#include <iostream>
#include <vector>
#include <queue>
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
    vector<int> rightSideView(TreeNode* root) {
        vector<int> ans;
        if (root==NULL) return ans;
        queue<TreeNode*> q;
        q.push(root);
        while (!q.empty()){
          int length = q.size();
          for(int i=0; i<length-1; i++){
            TreeNode* node = q.front();
            q.pop();
            if(node->left!=NULL) q.push(node->left);
            if(node->right!=NULL) q.push(node->right);
          }
          TreeNode* last = q.front();
          q.pop();
          ans.push_back(last->val);
          if(last->left!=NULL) q.push(last->left);
          if(last->right!=NULL) q.push(last->right);
        }
        return ans;
    }
};