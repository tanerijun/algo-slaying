class Solution:
	# Time complexity: O(n)
	# Space complexity: O(n)
	def longestConsecutive(self, nums: list[int]) -> int:
		res = 0
		numbers = set(nums)
		for num in numbers:
			# If there exist a number 1 size smaller than the current number, it can't possibly the start of the longest number sequence
			if num - 1 in numbers:
				continue

			# Since this num is potentially the start of the sequence, we can try to extend it
			length = 0
			while num + length in numbers:
				length += 1
				res = max(res, length)

		return res
