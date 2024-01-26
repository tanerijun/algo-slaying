function rearrangeArray(nums: number[]): number[] {
	// The idea is to put the number smaller then median in the odd index of the array
	// That way the neighbors of an index will be either both bigger than the number at the index
	// or both smaller than the number at the index.
	nums.sort((a, b) => a - b)
	const res: number[] = []

	let l = 0
	let r = nums.length - 1
	while (res.length !== nums.length) {
		res.push(nums[l])
		l++

		if (l <= r) {
			res.push(nums[r])
			r--
		}
	}

	return res
}
// Time complexity: O(n * log(n))
// Space complexity: O(1)
