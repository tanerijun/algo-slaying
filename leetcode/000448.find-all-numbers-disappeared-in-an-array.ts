function findDisappearedNumbers(nums: number[]): number[] {
	const disappearedNumbers: number[] = []
	const set = new Set<number>()

	for (let i = 0; i < nums.length; i++) {
		set.add(nums[i])
	}

	for (let i = 1; i <= nums.length; i++) {
		if (!set.has(i)) {
			disappearedNumbers.push(i)
		}
	}

	return disappearedNumbers
}
// Time complexity: O(n)
// Space complexity: O(n)
