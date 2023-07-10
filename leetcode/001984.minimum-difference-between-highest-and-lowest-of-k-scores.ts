function minimumDifference(nums: number[], k: number): number {
	nums.sort((a, b) => a - b)

	let l = 0
	let r = l + k - 1
	let min = Number.MAX_SAFE_INTEGER

	while (r < nums.length) {
		min = Math.min(min, nums[r] - nums[l])

		l++
		r++
	}

	return min
}
// Time complexity: O(n * log(n))
// Space complexity: O(1)
