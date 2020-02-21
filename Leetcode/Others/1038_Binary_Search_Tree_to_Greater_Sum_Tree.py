class Solution:
	def __init__(self):
		self.right_max = 0

	def bstToGst(self, root):
		if root.right is not None:
			self.bstToGst(root.right)

		root.val += self.right_max
		self.right_max = root.val

		if root.left is not None:
			self.bstToGst(root.left)

		return root
