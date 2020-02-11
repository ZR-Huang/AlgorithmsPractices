'''
You are given a perfect binary tree where all leaves are on the same level, 
and every parent has two children. The binary tree has the following definition:
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, 
the next pointer should be set to NULL.
Initially, all next pointers are set to NULL.

Follow up:
- You may only use constant extra space.
- Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.

Example 1:
Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), 
your function should populate each next pointer to point to 
its next right node, just like in Figure B. The serialized output 
is in level order as connected by the next pointers, 
with '#' signifying the end of each level.

Constraints:
- The number of nodes in the given tree is less than 4096.
- -1000 <= node.val <= 1000
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        '''
        A solution using O(n) extra space.
        '''
        if not root:
            return
        
        q = deque()
        q.append(root)
        while q:
            level_len = len(q)-1
            node = q.popleft()
            for _ in range(level_len):
                node.next = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                node = node.next
        
        return root

    def connect(self, root: 'Node') -> 'Node':
        '''
        Solve it recursively.
        '''
        if not root:
            return
        
        def helper(node):
            if not node.left: # if it is a leaf node
                return
            node.left.next = node.right # connect two children
            if node.next: # if grandchildren exist.
                node.right.next = node.next.left # connect two grandchildren
            helper(node.left)
            helper(node.right)
            
        helper(root)
        return root