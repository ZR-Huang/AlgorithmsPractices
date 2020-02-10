'''
Given a binary tree, return the zigzag level order traversal of its nodes' values. 
(ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7

return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        stack = [root]
        ans = []

        level = 1
        while stack:
            level_node = []
            level_output = []
            for _ in range(len(stack)):
                level_node.append(stack.pop())
            
            if level & 1:   # odd level
                for node in level_node:
                    level_output.append(node.val)
                    if node.left:
                        stack.append(node.left)
                    if node.right:
                        stack.append(node.right)
            else:           # even level
                for node in level_node:
                    level_output.append(node.val)
                    # level_output.reverse()
                    if node.right:
                        stack.append(node.right)
                    if node.left:
                        stack.append(node.left)

            level += 1
            ans.append(level_output)
        return ans