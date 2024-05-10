from collections import defaultdict


class Solution:
	# Time complexity: O(9 ^ 2)
	# Space complexity: O(9 ^ 2)
	def isValidSudoku(self, board: list[list[str]]) -> bool:
		rows = defaultdict(set)
		cols = defaultdict(set)
		blocks = defaultdict(set) # key = (row // 3, col // 3)

		for row in range(len(board)):
			for col in range(len(board)):
				cur = board[row][col]
				if cur == ".":
					continue
				if (cur in rows[row] or
					cur in cols[col] or
					cur in blocks[(row // 3, col // 3)]):
					return False
				rows[row].add(cur)
				cols[col].add(cur)
				blocks[(row // 3, col // 3)].add(cur)

		return True
