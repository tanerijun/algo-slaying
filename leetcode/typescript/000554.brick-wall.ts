function leastBricks(wall: number[][]): number {
	// The ideal place to draw a line that crossed the least amount of block is after
	// the common prefix sum with the highest count.
	const prefixSumCount = new Map<number, number>()

	for (const bricks of wall) {
		let sum = 0

		// We can skip the last one, because it's the edge
		for (let i = 0; i < bricks.length - 1; i++) {
			sum += bricks[i]
			prefixSumCount.set(sum, (prefixSumCount.get(sum) ?? 0) + 1)
		}
	}

	const mapValues = Array.from(prefixSumCount.values())

	return mapValues.length > 0
		? wall.length - Math.max(...mapValues)
		: wall.length
}

// Time complexity: O(n)  n = number of bricks
// Space complexity: O(m) m = width of the wall
