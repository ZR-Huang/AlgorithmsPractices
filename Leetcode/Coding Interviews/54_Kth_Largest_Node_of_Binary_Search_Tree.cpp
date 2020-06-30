/*
给定一棵二叉搜索树，请找出其中第k大的节点。

示例 1:
输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 4

示例 2:
输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 4
 
限制：
1 ≤ k ≤ 二叉搜索树元素个数
*/

#include <iostream>
#include <stack>
#include <vector>
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
    int kthLargest(TreeNode* root, int k) {
        stack<TreeNode*> s;
        vector<int> res;
        TreeNode* currNode = root;
        while((currNode != NULL) || !s.empty()){
            while (currNode != NULL)
            {
                s.push(currNode);
                currNode = currNode->left;
            }
            currNode = s.top();
            s.pop();
            res.push_back(currNode->val);
            currNode = currNode->right;
        }
        return res[res.size()-k];
    }

    int kthLargest(TreeNode* root, int k) {
        // reverse order of inorder traversal
        stack<TreeNode*> s;
        int count = 0, res = 0;
        TreeNode* currNode = root;
        while((currNode != NULL) || !s.empty()){
            while (currNode != NULL)
            {
                s.push(currNode);
                currNode = currNode->right;
            }
            currNode = s.top();
            s.pop();
            count++;
            if(count == k) {
                res = currNode->val;
                return res;
            }
            currNode = currNode->left;
        }
        return res;
    }
};