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

function findDisappearedNumbers2(nums: number[]): number[] {
	const disappearedNumbers: number[] = []

	// Instead of using a set, we can modify the array in place
	// The input array nums: 1..n map to index 0..n-1 in the array; It's a -1 relationship
	// Whenever we find a number, we can mark nums[nums[i] - 1] as negative
	// And we return positive num in nums

	function toNegative(n: number) {
		return n <= 0 ? n : n * -1
	}

	for (let i = 0; i < nums.length; i++) {
		nums[Math.abs(nums[i]) - 1] = toNegative(nums[Math.abs(nums[i]) - 1])
	}

	for (let i = 0; i <= nums.length; i++) {
		if (nums[i] > 0) {
			disappearedNumbers.push(i + 1)
		}
	}

	return disappearedNumbers
}
// Time complexity: O(n)
// Space complexity: O(n)
