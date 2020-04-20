/*
请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，
第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。

例如:
给定二叉树: [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7

返回其层次遍历结果：
[
  [3],
  [20,9],
  [15,7]
]

提示：
    节点总数 <= 1000
*/
#include <iostream>
#include <vector>
#include <queue>
#include <stack>
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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> ans;
        if (root==NULL) return ans;
        int left_to_right = -1;
        stack<TreeNode*> s, helper_s;
        s.push(root);
        while(!s.empty()){
            int length = s.size();
            vector<int> level;
            for (int i=0; i<length; i++){
                TreeNode* node = s.top();
                s.pop();
                level.push_back(node->val);
                if (left_to_right > 0){
                    if(node->right!=NULL) helper_s.push(node->right);
                    if(node->left!=NULL) helper_s.push(node->left);
                }
                else {
                    if(node->left!=NULL) helper_s.push(node->left);
                    if(node->right!=NULL) helper_s.push(node->right);
                }
            }
            left_to_right *= -1;
            ans.push_back(level);
            s.swap(helper_s);
        }
        return ans;
    }
};