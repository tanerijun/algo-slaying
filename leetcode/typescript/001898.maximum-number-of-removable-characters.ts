function maximumRemovals(s: string, p: string, removable: number[]): number {
	// Keep track of index of chars we've removed from s
	// We use set, so that we can check it's member in O(1)
	let removed: Set<number>;
	let res = 0;

	function isSubsequence() {
		let i1 = 0; // tracks string
		let i2 = 0; // tracks substring

		while (i1 < s.length && i2 < p.length) {
			// Also skip if the char is already removed
			if (removed.has(i1) || s[i1] !== p[i2]) {
				i1++;
				continue;
			}

			i1++;
			i2++;
		}

		return i2 === p.length;
	}

	// Run binary search on removable
	let l = 0;
	let r = removable.length - 1;

	while (l <= r) {
		const m = Math.floor((l + r) / 2);
		removed = new Set(removable.slice(0, m + 1));

		if (isSubsequence()) {
			res = Math.max(res, m + 1); // m + 1 because m is the index, but we want the number of elements to skip
			l = m + 1;
		} else {
			r = m - 1;
		}
	}

	return res;
}
// Time complexity: O(n * log(k))
// Space complexity: O(k)
