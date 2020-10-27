/*
144. Binary Tree Preorder Traversal

Given the root of a binary tree, return the preorder traversal of its nodes' values.
 
Example 1:
Input: root = [1,null,2,3]
Output: [1,2,3]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

Example 4:
Input: root = [1,2]
Output: [1,2]

Example 5:
Input: root = [1,null,2]
Output: [1,2]
 
Constraints:
	The number of nodes in the tree is in the range [0, 100].
	-100 <= Node.val <= 100

Follow up:
Recursive solution is trivial, could you do it iteratively?
*/

#include <iostream>
#include <vector>
#include <stack>
using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    vector<int> ans;
    vector<int> preorderTraversal(TreeNode* root) {
        // recursive solution
        if(root == nullptr) return ans;
        
        ans.push_back(root->val);
        preorderTraversal(root->left);
        preorderTraversal(root->right);

        return ans;
    }

    vector<int> preorderTraversal(TreeNode* root) {
        // iterative solution
        stack<TreeNode*> s;
        if(root == nullptr) return ans;
        s.push(root);
        while(!s.empty()){
            TreeNode* node = s.top();
            s.pop();
            ans.push_back(node->val);
            if(node->right!=nullptr)
                s.push(node->right);
            if(node->left!=nullptr)
                s.push(node->left);
        }
        return ans;
    }
};