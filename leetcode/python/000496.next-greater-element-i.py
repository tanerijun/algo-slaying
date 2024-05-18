class Solution:
	# Time complexity: O(m + n)
	# Space complexity: O(m)
	def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
		map = {n:i for i, n in enumerate(nums1)}
		stack = []
		res = [-1] * len(nums1)

		for n in nums2:
			while stack and n > stack[-1]:
				popped = stack.pop()
				res[map[popped]] = n

			if n in map:
				stack.append(n)

		return res
