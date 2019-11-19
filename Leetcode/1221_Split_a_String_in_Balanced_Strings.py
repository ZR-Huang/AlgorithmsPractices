class Solution:
	def balancedStringSplit(self, s):
		result = 0
		substring_r_amount = 0
		substring_l_amount = 0
		for c in s:
			if c == 'R':
				substring_r_amount += 1
			else:
				substring_l_amount += 1
			if substring_l_amount == substring_r_amount:
				result += 1
				substring_r_amount = 0
				substring_l_amount = 0

		return result

	def balancedStringSplit2(self,s):
		result = 0
		balanced_ = 0
		for c in s:
			balanced_ += c == 'L' and 1 or -1
			if balanced_ == 0:
				result += 1
		return result

s = "RLRRLLRLRL"
print(Solution().balancedStringSplit2(s))

