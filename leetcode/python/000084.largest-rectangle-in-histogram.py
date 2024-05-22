class Solution:
	# Time complexity: O(n)
	# Space complexity: O(n)
	def largestRectangleArea(self, heights: list[int]) -> int:
		max_area = 0
		stack = [] # contains tuple (index, height)

		for i in range(len(heights)):
			if len(stack) == 0 or heights[i] > stack[-1][1]:
				stack.append((i, heights[i]))
				continue

			smallest_idx = len(heights)
			# Pop stack to maintain the monotonic increasing property
			while (len(stack) > 0 and heights[i] <= stack[-1][1]):
				pop_idx, pop_height = stack.pop()
				smallest_idx = pop_idx
				width = i - pop_idx
				area = pop_height * width
				max_area = max(max_area, area)

			# Append tuple (index, height) to stack
			# But in this case, the index is the idx of the last element we pop
			# Why? Because we're expanding to the left
			# Since the elements we popped are bigger then the current height
			# That means the current height can be expanded to the left
			# Ex: [3 2], the 2 can be expanded to the left, which will result in area of 4 later
			stack.append((smallest_idx, heights[i]))

		# Handle leftovers in stack
		# Each item in the stack at this point can be expanded all the way to the right
		# After all, they're not popped, that means they're in increasing order
		# Ex: [1 2 3]
		for idx, height in stack:
			area = height * (len(heights) - idx)
			max_area = max(max_area, area)

		return max_area
