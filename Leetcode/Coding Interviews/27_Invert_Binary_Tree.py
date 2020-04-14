'''
注意：本题与主站 226 题相同：https://leetcode-cn.com/problems/invert-binary-tree/

请完成一个函数，输入一个二叉树，该函数输出它的镜像。

例如输入：
     4
   /   \
  2     7
 / \   / \
1   3 6   9
镜像输出：
     4
   /   \
  7     2
 / \   / \
9   6 3   1

示例 1：
输入：root = [4,2,7,1,3,6,9]
输出：[4,7,2,9,6,3,1]

限制：
0 <= 节点个数 <= 1000
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        if root.left and root.right:
            root.left, root.right = root.right, root.left
            self.mirrorTree(root.left)
            self.mirrorTree(root.right)
        elif (not root.left) and root.right:
            root.left = root.right
            root.right = None
            self.mirrorTree(root.left)
        elif (not root.right) and root.left:
            root.right = root.left
            root.left = None
            self.mirrorTree(root.right)
        return root