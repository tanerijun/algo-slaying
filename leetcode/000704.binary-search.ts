function search(nums: number[], target: number): number {
	let l = 0;
	let r = nums.length - 1;

	while (l <= r) {
		const mid = Math.floor((r + l) / 2);
		if (nums[mid] < target) {
			l = mid + 1;
		} else if (nums[mid] > target) {
			r = mid - 1;
		} else {
			return mid;
		}
	}

	return -1;
}
// Time complexity: O(n)
// Space complexity: O(1)
