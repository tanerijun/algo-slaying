function searchInsert(nums: number[], target: number): number {
	let l = 0;
	let r = nums.length - 1;

	while (l <= r) {
		const m = Math.floor((l + r) / 2);
		if (target > nums[m]) {
			l = m + 1;
		} else if (target < nums[m]) {
			r = m - 1;
		} else {
			return m;
		}
	}

	return nums[r] > target ? r : r + 1;
}
// Time complexity: O(n)
// Space complexity: O(1)
