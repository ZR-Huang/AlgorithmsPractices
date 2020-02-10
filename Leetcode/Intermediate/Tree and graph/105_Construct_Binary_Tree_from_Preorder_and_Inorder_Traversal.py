'''
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

Return the following binary tree:
    3
   / \
  9  20
    /  \
   15   7
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def helper(preorder, inorder):
            if (not preorder):
                return
            root = TreeNode(preorder[0]) # get the value of the root
            # find root in the inorder list
            for i, value in enumerate(inorder):
                if value == root.val:
                    root_index = i
                    break
            # get number of nodes of the left child
            left_number = i
            if root_index != 0: # the number of nodes in inorder list is more than one node.
                root.left = helper(preorder[1:1+left_number], inorder[:left_number])
                root.right = helper(preorder[1+left_number:], inorder[left_number+1:])
            return root

        if not preorder:
            return   
        root = helper(preorder, inorder)
        return root