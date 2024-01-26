function findMin(nums: number[]): number {
	let l = 0;
	let r = nums.length - 1;
	let res = Number.MAX_SAFE_INTEGER;

	while (l <= r) {
		// Check if search range already sorted
		if (nums[l] < nums[r]) {
			return Math.min(res, nums[l]);
		}

		const m = Math.floor((l + r) / 2);
		res = Math.min(res, nums[m]);

		if (nums[m] >= nums[l]) {
			l = m + 1;
		} else {
			r = m - 1;
		}
	}

	return res;
}
// Time complexity: O(n)
// Space complexity: O(1)
