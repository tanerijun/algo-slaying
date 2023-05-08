function runningSum(nums: number[]): number[] {
	const res = new Array(nums.length).fill(0)

	res[0] = nums[0]

	for (let i = 1; i < nums.length; i++) {
		res[i] = nums[i] + res[i - 1]
	}

	return res
}
// Time complexity: O(n)
// Space complexity: O(n)

function runningSum2(nums: number[]): number[] {
	for (let i = 1; i < nums.length; i++) {
		nums[i] = nums[i] + nums[i - 1]
	}

	return nums
}
// Time complexity: O(n)
// Space complexity: O(1)
