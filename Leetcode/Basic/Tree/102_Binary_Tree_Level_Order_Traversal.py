'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def levelOrder(self, root):
        q = deque()
        q.append(root)
        ans = []

        while q:
            length = len(q)
            level_vals = []
            for _ in range(length):
                node = q.popleft()
                if node:
                    level_vals.append(node.val)
                    q.append(node.left)
                    q.append(node.right)

            if level_vals:
                ans.append(level_vals)
        
        return ans