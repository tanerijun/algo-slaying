class Solution:
	# Time complexity: O(n)
	# Space complexity: O(1)
	def twoSum(self, numbers: list[int], target: int) -> list[int]:
		res = []
		l, r = 0, len(numbers) - 1
		while l < r:
			sum = numbers[l] + numbers[r]
			if sum < target:
				l += 1
			elif sum > target:
				r -= 1
			else:
				res = [l+1, r+1]
				break
		return res
