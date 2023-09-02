function findPeakElement(nums: number[]): number {
	let l = 0;
	let r = nums.length - 1;

	while (l <= r) {
		const m = Math.floor((l + r) / 2);

		// How do we decide whether to search left or right?
		// We search right if m + 1 > m and left if m - 1 > m
		// Intuition:
		// Possibility 1:
		//     x
		//   x
		// m
		// Possibility 2:
		//   x
		// m
		//     x
		// Since the peak can be in both size, we just need to choose the side that's guaranteed to have a peak.
		// As you can see above, as long as the num after m is bigger than m, it doesn't matter if the next num is a dip, or peak, there'll always be a peak.

		if (m < nums.length - 1 && nums[m + 1] > nums[m]) {
			l = m + 1;
		} else if (m > 0 && nums[m - 1] > nums[m]) {
			r = m - 1;
		} else {
			return m;
		}
	}

	return -1; // shouldn't happen
}
// Time complexity: O(n)
// Space complexity: O(1)
