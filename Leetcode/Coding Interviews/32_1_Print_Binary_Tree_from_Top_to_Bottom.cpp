/*
从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。

例如:
给定二叉树: [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7

返回：
[3,9,20,15,7]

提示：
    节点总数 <= 1000
*/
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

/**
 * Definition for a binary tree node.*/
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    vector<int> levelOrder(TreeNode* root) {
        queue<TreeNode*> q;
        vector<int> ans;
        if (root==NULL){
            return ans;
        }
        q.push(root);
        while (!q.empty()){
            int length = q.size();
            for (int i=0; i<length; i++){
                TreeNode* node = q.front();
                q.pop();
                if (node->left!=NULL) q.push(node->left);
                if (node->right!=NULL) q.push(node->right);
                ans.push_back(node->val);
            }
        }
        return ans;
    }
};