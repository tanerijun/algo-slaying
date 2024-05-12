class Solution:
	# Time complexity: O(n)
	# Space complexity: O(n) // due to Timsort
	def threeSum(self, nums: list[int]) -> list[list[int]]:
		res = []
		nums.sort()
		for i in range(len(nums) - 2):
			# Skip duplicates
			if i > 0 and nums[i-1] == nums[i]:
				continue

			cur = nums[i]
			complement = 0 - nums[i] # our target sum is 0
			j, k = i + 1, len(nums) - 1
			while j < k:
				sum = nums[j] + nums[k]
				if sum > complement:
					k -= 1
				elif sum < complement:
					j += 1
				else:
					res.append([cur, nums[j], nums[k]])
					j += 1
					# Skip duplicates
					while nums[j] == nums[j-1] and j < k:
						j += 1
		return res
