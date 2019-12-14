'''
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

Example 1:
    2
   / \
  1   3
Input: [2,1,3]
Output: true

Example 2:
    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # Leverage the inorder traversal result,
        # because the result of the inoder traversal result of a 
        # binary tree is the sorted array
        array = [] # store the result of the inorder traversal

        def inorder_traversal(root, array):
            if not root:
                return 
            
            if not root.left and not root.right:
                array.append(root.val)
                return 
            
            if root.left:
                inorder_traversal(root.left, array)
            array.append(root.val)
            if root.right:
                inorder_traversal(root.right)
        
        inorder_traversal(root, array)

        if len(array) == 0:
            return False
        
        if len(array) == 1:
            return True
        
        for i in range(1, len(array)):
            if array[i] <= array[i-1]:
                return False
        return True
            

        

            
        
