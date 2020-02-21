'''
Given a binary tree, return the postorder traversal of its nodes' values.

Example:
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]

Follow up: Recursive solution is trivial, could you do it iteratively?
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        '''
        Iterative solution
        
        reversion of modified preorder traversal
        preorder: root -> left -> right
        postorder: left -> right -> root
        '''
        if not root:
            return []
        
        stack = [root]
        ans = []
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            ans.append(node.val)

        return ans[::-1]
    
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        '''
        Iterative solution
        
        strictly follow the postorder
        postorder: left -> right -> root
        '''
        if not root:
            return []
        
        stack = [root]
        ans = []
        visited = set()
        while stack:
            node = stack[-1]
            
            left_visited, right_visited = True, True
            if node.right and (node.right not in visited):
                stack.append(node.right)
                right_visited = False
            
            if node.left and (node.left not in visited):
                stack.append(node.left)
                left_visited = False
            
            if left_visited and right_visited:
                curr = stack.pop()
                ans.append(curr.val)
                visited.add(curr)

        return ans