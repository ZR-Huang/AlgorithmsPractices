'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
    1
   / \
  2   2
 / \ / \
3  4 4  3

But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def isSymmetric(self, root) -> bool:
        q = deque()
        q.append(root)

        while q:
            level_vals = []
            length = len(q)
            for _ in range(length):
                node = q.popleft()
                if node:
                    level_vals.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                else:
                    level_vals.append(None)
                

            l = 0
            r = length - 1
            while l < r and level_vals:
                if level_vals[l] != level_vals[r]:
                    return False
                else:
                    l += 1
                    r -= 1
        
        return True