function maxFrequency(nums: number[], k: number): number {
	nums.sort((a, b) => a - b);

	let res = 0;
	let l = 0;
	let r = 0;
	let sum = 0;

	while (r < nums.length) {
		sum += nums[r];

		// While window is invalid
		while (nums[r] * (r - l + 1) > sum + k) {
			sum -= nums[l];
			l++;
		}

		res = Math.max(res, r - l + 1);
		r++;
	}

	return res;
}
// Time complexity: O(n * log(n))
// Space complexity: O(1)
