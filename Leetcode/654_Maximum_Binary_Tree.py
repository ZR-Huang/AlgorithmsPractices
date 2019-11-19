# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
		if not nums:
			return None
		max_value = max(nums)
		max_index = nums.index(max_value)

		node = TreeNode(max_value)
		node.left = self.constructMaximumBinaryTree(nums[:max_index])
		node.right = self.constructMaximumBinaryTree(nums[max_index + 1:])

		return node