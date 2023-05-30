function majorityElement(nums: number[]): number {
	let max: [k: number, v: number] = [0, 0] // tuple: [k, v]
	const map = new Map<number, number>()

	for (let i = 0; i < nums.length; i++) {
		map.set(nums[i], (map.get(nums[i]) || 0) + 1)
	}

	for (const [k, v] of map) {
		if (v > max[1]) {
			max = [k, v]
		}
	}

	return max[0]
}
// Time complexity: O(n)
// Space complexity: O(n)
