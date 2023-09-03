function minimizeMax(nums: number[], p: number): number {
	if (p === 0) {
		return 0;
	}

	nums.sort((a, b) => a - b);

	// Linear search on nums
	// Search for pairs with differences == m
	// Check if the pair count is p
	function isValid(threshold: number) {
		let i = 0;
		let pairCount = 0;

		while (i < nums.length - 1) {
			if (Math.abs(nums[i] - nums[i + 1]) <= threshold) {
				pairCount++;
				i += 2;
			} else {
				i += 1;
			}

			if (pairCount === p) {
				return true;
			}
		}

		return false;
	}

	// Running binary search on possible answers
	let l = 0;
	let r = nums[nums.length - 1] - nums[0]; // The max diff of any pair is bounded by max(nums) - min(nums)
	let res = Number.MAX_SAFE_INTEGER;

	while (l <= r) {
		const m = Math.floor((l + r) / 2);

		if (isValid(m)) {
			res = m;
			r = m - 1;
		} else {
			l = m + 1;
		}
	}

	return res;
}
// Time complexity: O(n(log(m))) -- m = max(nums) - min(nums)
// Space complexity: O(1)
