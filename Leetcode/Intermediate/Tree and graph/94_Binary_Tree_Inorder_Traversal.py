'''
Given a binary tree, return the inorder traversal of its nodes' values.

Example:
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]

Follow up: Recursive solution is trivial, could you do it iteratively?
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        '''
        Recursive solution
        '''
        def recursive(root, ans):
            if not root:
                return
            
            recursive(root.left, ans)
            if root.val:
                ans.append(root.val)
            recursive(root.right, ans)
        
        ans = []
        recursive(root, ans)
        return ans

    
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        '''
        Iterative solution
        '''
        stack = []
        ans = []
        
        curr_node = root
        while (not curr_node) or stack:
            while not curr_node:
                stack.append(curr_node)
                curr_node = curr_node.left
            
            curr_node = stack.pop()
            if curr_node.val:
                curr_node.append(curr_node.val)
            curr_node = curr_node.right
        
        return ans

                    
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        '''
        Morris Algorithm
        '''
        ans = []

        curr_node = root
        while curr_node:
            if not curr_node.left:
                if curr_node.val:
                    ans.append(curr_node.val)
                curr_node = curr_node.right
            else:
                pre_node = curr_node.left    #Precursor
                while pre_node.right:
                    pre_node = pre_node.right       # move to the rightmost node
                pre_node.right = curr_node
                tmp = curr_node     # store current node
                curr_node = curr_node.left  # move current to the top of the new tree
                tmp.left = None 
        
        return ans