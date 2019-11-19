class Solution:
	def removeOuterParentheses(self, S):
		left_parenthes_count = 0
		right_parenthes_count = 0

		decompositions = []

		last_decompose_index = 0
		for index, c in enumerate(S):
			if c == '(':
				left_parenthes_count += 1
			else:
				right_parenthes_count += 1

			if left_parenthes_count == right_parenthes_count:
				decompositions.append(S[last_decompose_index:index + 1])

				left_parenthes_count = 0
				right_parenthes_count = 0
				last_decompose_index = index+1

		return ''.join([item[1:-1] for item in decompositions])


print(Solution().removeOuterParentheses("(()())(())"))