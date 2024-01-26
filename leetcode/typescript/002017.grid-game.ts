function gridGame(grid: number[][]): number {
	const N = grid[0].length
	const prefixSumRowOne = [...grid[0]]
	const prefixSumRowTwo = [...grid[1]]

	for (let i = 1; i < N; i++) {
		prefixSumRowOne[i] += prefixSumRowOne[i - 1]
		prefixSumRowTwo[i] += prefixSumRowTwo[i - 1]
	}

	/**
	 * Notice how after robot A move, the grid will be divided into 2.
	 * Robot B will have to choose whether it want to traverse the top right path,
	 * or bottom left path.
	 *
	 * Illustration:
	 * 0 0 n    0 0 0    0 n n
	 * n 0 0    n n 0    0 0 0
	 */
	let res = Number.MAX_SAFE_INTEGER

	for (let i = 0; i < N; i++) {
		const top = prefixSumRowOne[N - 1] - prefixSumRowOne[i]
		const bottom = i > 0 ? prefixSumRowTwo[i - 1] : 0
		const robotB = Math.max(top, bottom)
		res = Math.min(res, robotB)
	}

	/**
	 * The loop above basically look for every possible value for robot B.
	 * The reason why we take the minimum is because if robot A play optimally,
	 * robot B will naturally be left with the minimum value.
	 */

	return res
}
// Time complexity: O(n)
// Space complexity: O(n)
