function pickingNumbers(a: number[]): number {
	let maxLength = 0
	const countMap = new Map<number, number>()

	for (const num of a) {
		countMap.set(num, (countMap.get(num) || 0) + 1)
	}

	for (const key of countMap.keys()) {
		maxLength = Math.max(
			maxLength,
			countMap.get(key)! + (countMap.get(key + 1) || 0)
		)
	}

	return maxLength
}
// Time complexity: O(n)
