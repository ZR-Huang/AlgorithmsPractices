/*
注意：本题与主站 297 题相同：https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/

请实现两个函数，分别用来序列化和反序列化二叉树。

示例: 
你可以将以下二叉树：
    1
   / \
  2   3
     / \
    4   5

序列化为 "[1,2,3,null,null,4,5]"
*/

#include <iostream>
#include <string>
#include <queue>
#include <sstream>
#include <algorithm>
using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Codec {
public:

    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        if (root == NULL) return "";
        queue<TreeNode*> q;
        vector<string> ans;
        q.push(root);
        while(!q.empty()){
            int length = q.size();
            for (int i=0; i<length ; i++){
                TreeNode* node = q.front();
                q.pop();
                if (node == NULL) ans.push_back("null");
                else {
                    ans.push_back(to_string(node->val));
                    q.push(node->left);
                    q.push(node->right);
                }
            }
        }
        stringstream ss;
        for(int i=0; i<ans.size(); i++)
        {
            if(i != 0) ss << ",";
            ss << ans[i];
        }
        return ss.str();
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        if(data.empty()) return NULL;
        vector<string> values;
        stringstream ss(data);
        while(ss.good()){
            string substr;
            getline(ss, substr, ',');
            values.push_back(substr);
        }
        reverse(values.begin(), values.end());
        queue<TreeNode*> q;
        TreeNode* root = new TreeNode(stoi(values.at(values.size()-1)));
        values.pop_back();
        q.push(root);
        while(!q.empty()){
            int length = q.size();
            for(int i=0; i<length; i++){
                TreeNode* node = q.front();
                q.pop();
                string left = values.at(values.size()-1);
                values.pop_back();
                string right = values.at(values.size()-1);
                values.pop_back();
                if (left != "null"){
                    node->left = new TreeNode(stoi(left));
                    q.push(node->left);
                }
                if (right != "null"){
                    node->right = new TreeNode(stoi(right));
                    q.push(node->right);
                }
            }
        }
        return root;
    }
};

int main(){
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->right->left = new TreeNode(4);
    root->right->right = new TreeNode(5);
    Codec c;
    c.deserialize(c.serialize(root));
    return 0;
}
// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.deserialize(codec.serialize(root));