'''
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:
Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
 '''

 # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        
        if len(nums) == 1:
            return TreeNode(nums[0])
        
        def helper(l, r):
            if l + 1 == r:
                root = TreeNode(nums[r])
                root.left = TreeNode(nums[l])
                return root
            elif l + 2 == r:
                root = TreeNode(nums[(l+r)>>1])
                root.left = TreeNode(nums[l])
                root.right = TreeNode(nums[r])
                return root
            else:
                mid = (l+r) >> 1
                root = TreeNode(nums[mid])
                root.left = helper(l, mid-1)
                root.right = helper(mid+1, r)
                return root
        
        root = helper(0, len(nums)-1)
        return root

