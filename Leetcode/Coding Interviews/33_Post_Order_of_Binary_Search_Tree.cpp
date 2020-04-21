/*
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。
假设输入的数组的任意两个数字都互不相同。

参考以下这颗二叉搜索树：
     5
    / \
   2   6
  / \
 1   3

示例 1：
输入: [1,6,3,2,5]
输出: false

示例 2：
输入: [1,3,2,6,5]
输出: true

提示：
    数组长度 <= 1000
*/
#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    bool verifyPostorder(vector<int>& postorder) {
        return helper(postorder, 0, postorder.size()-1);
    }

    bool helper(vector<int>& postorder, int start, int end){
        if (start >= end) return true;
        int root = postorder[end];
        int split_index = start;
        for (; split_index<end; split_index++)
            if (postorder[split_index] > root) 
                break;
        for (int i=split_index; i<end; i++){
            if (postorder[i] < root) return false;
        }
        return helper(postorder, start, split_index-1) && helper(postorder, split_index, end-1);
    }
};