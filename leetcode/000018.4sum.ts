function fourSum(nums: number[], target: number): number[][] {
	nums.sort((a, b) => a - b)

	return kSum(nums, target, 4)
}
// Time complexity: O(n^3)
// Space complexity: O(1)

// The idea here is that three sum builds after two sum,
// and four sum builds after three sums, ...
// With kSum, it's possible to also solve 5sum, 6sum, ...
// Using two pointer, so input array has to be sorted
function kSum(nums: number[], target: number, k: number) {
	const res: number[][] = []

	if (k < 2) {
		return []
	}

	if (k === 2) {
		return twoSum(nums, target)
	}

	for (let i = 0; i <= nums.length - k; i++) {
		// Skip duplicates
		if (i > 0 && nums[i] === nums[i - 1]) {
			continue
		}

		const kMinusOneSum = kSum(nums.slice(i + 1), target - nums[i], k - 1)

		for (const result of kMinusOneSum) {
			res.push([nums[i]].concat(result))
		}
	}

	return res
}

// Return array of all the unique pair of nums that sum to target
// Using two pointer, so input array has to be sorted
function twoSum(nums: number[], target: number) {
	const res: number[][] = []

	let l = 0
	let r = nums.length - 1
	while (l < r) {
		// Skip duplicates
		if (l > 0 && nums[l] === nums[l - 1]) {
			l++
			continue
		}

		const sum = nums[l] + nums[r]
		if (sum < target) {
			l++
		} else if (sum > target) {
			r--
		} else {
			res.push([nums[l], nums[r]])
			l++
			r--
		}
	}

	return res
}
