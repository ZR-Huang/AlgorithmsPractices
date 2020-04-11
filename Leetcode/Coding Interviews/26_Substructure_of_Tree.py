'''
输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)
B是A的子结构， 即 A中有出现和B相同的结构和节点值。

例如:
给定的树 A:
     3
    / \
   4   5
  / \
 1   2
给定的树 B：
   4 
  /
 1
返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。

示例 1：
输入：A = [1,2,3], B = [3,1]
输出：false

示例 2：
输入：A = [3,4,5,1,2], B = [4,1]
输出：true

限制：
0 <= 节点个数 <= 10000
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not A or not B:
            return False
        if A.val != B.val:
            if self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B):
                return True
        else:
            if self.isSubTree(A, B):
                return True
        return False
    
    def isSubTree(self, A, B):
        # when roots of A an B are same.
        if A and A.val == B.val:
            left, right = 0, 0
            if not B.left and not B.right:
                return True
            if B.left:
                left = self.isSubTree(A.left, B.left)
            if B.right:
                right = self.isSubTree(A.right, B.right)
            if B.left and B.right:
                return left and right
            else:
                return left or right
        else:
            return False


A = TreeNode(10)
A.left = TreeNode(12)
A.right = TreeNode(6)
A.left.left = TreeNode(8)
A.left.right = TreeNode(3)
A.right.left = TreeNode(11)
B = TreeNode(10)
B.left = TreeNode(12)
B.right = TreeNode(6)
B.left.left = TreeNode(8)
print(Solution().isSubStructure(A, B))