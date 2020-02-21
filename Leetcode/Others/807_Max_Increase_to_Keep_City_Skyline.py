class Solution:
	def maxIncreaseKeepingSkyline(self, grid):
		row_max_list = [0 for _ in range(len(grid))]
		column_max_list = [0 for _ in range(len(grid))]
		for i in range(len(grid)):
			for j in range(len(grid[0])):
				if grid[i][j] > row_max_list[i]:
					row_max_list[i] = grid[i][j]
				if grid[i][j] > column_max_list[j]:
					column_max_list[j] = grid[i][j]

		sum_ = 0
		for i in range(len(grid)):
			for j in range(len(grid[0])):
				sum_ += row_max_list[i] - grid[i][j] if row_max_list[i]<column_max_list[j] else column_max_list[j]-grid[i][j]

		return sum_

	def maxIncreaseKeepingSkyline2(self, grid):
		row_max_list = [max(row) for row in grid]
		column_max_list = [max(col) for col in zip(*grid)]

		sum_ = 0
		for i in range(len(grid)):
			for j in range(len(grid[0])):
				sum_ += min(row_max_list[i], column_max_list[j]) - grid[i][j]

		return sum_

grid = [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]
print(Solution().maxIncreaseKeepingSkyline2(grid))

