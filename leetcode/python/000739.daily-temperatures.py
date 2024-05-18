class Solution:
	# Time complexity: O(n)
	# Space complexity: O(n)
	def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
		stack = [] # monotonic decreasing stack
		res = [0] * len(temperatures)
		for i in range (len(temperatures)):
			while stack and temperatures[i] > stack[-1][0]:
				val, idx = stack.pop()
				res[idx] = i - idx
			stack.append((temperatures[i], i))
		return res
