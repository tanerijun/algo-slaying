class Solution:
	# Time complexity: O(n)
	# Space complexity: O(1)
	def maxArea(self, height: list[int]) -> int:
		max_area = 0
		l, r = 0, len(height) - 1
		while l < r:
			area = min(height[l], height[r]) * (r - l)
			max_area = max(area, max_area)
			if height[l] <= height[r]:
				l += 1
			else:
				r -= 1
		return max_area
