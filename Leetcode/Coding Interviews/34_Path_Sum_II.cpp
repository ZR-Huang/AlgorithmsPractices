/*
输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。
从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。

示例:
给定如下二叉树，以及目标和 sum = 22，
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1

返回:
[
   [5,4,11,2],
   [5,8,4,5]
]

提示：
    节点总数 <= 10000
*/

#include <iostream>
#include <vector>
using namespace std;

//Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
private:
    vector<vector<int>> ans;
public:
    vector<vector<int>> pathSum(TreeNode* root, int sum) {
        if(root==NULL) return ans;
        vector<int> path;
        search(root, sum, path);
        return ans;
    }
    void search(TreeNode* root, int sum, vector<int> path){
        path.push_back(root->val);
        sum -= root->val;
        if(sum==0 && root->left==NULL && root->right==NULL)
            ans.push_back(path);
        if(root->left!=NULL) search(root->left, sum, path);
        if(root->right!=NULL) search(root->right, sum, path);
    }
};

int main(){
    TreeNode* root = new TreeNode(5);
    // root->val = 5;
    root->left= new TreeNode(4), root->right = new TreeNode(8);
    root->left->left=new TreeNode(11), root->right->left=new TreeNode(13), root->right->right=new TreeNode(4);
    root->left->left->left=new TreeNode(7), root->left->left->right=new TreeNode(2);
    root->right->right->left=new TreeNode(5), root->right->right->right= new TreeNode(1);
    Solution s;
    vector<vector<int>> ans = s.pathSum(root, 22);
    return 0;
}