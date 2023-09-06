function search(nums: number[], target: number): boolean {
	let l = 0;
	let r = nums.length - 1;

	while (l <= r) {
		const m = Math.floor((l + r) / 2);

		if (target === nums[m]) {
			return true;
		}

		// If this condition is true, we can't be sure if nums[m] is part of the left portion or right portion.
		// Ex: 2 2 2 1 2 2
		// So, we just skip it, and restart our search
		// In the worst case, this'll make our time complexity: O(n)
		// But on average, it's still better than linear
		if (nums[l] === nums[m]) {
			l++;
			continue;
		}

		if (nums[l] <= nums[m]) {
			if (target < nums[m] && target >= nums[l]) {
				r = m - 1;
			} else {
				l = m + 1;
			}
		} else {
			if (target > nums[m] && target <= nums[r]) {
				l = m + 1;
			} else {
				r = m - 1;
			}
		}
	}

	return false;
}
// Time complexity: O(n)
// Space complexity: O(1)
