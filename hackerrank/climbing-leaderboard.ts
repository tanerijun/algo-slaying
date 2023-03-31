function climbingLeaderboard(ranked: number[], player: number[]): number[] {
	const res: number[] = []
	const set = new Set(ranked)
	const ranks = [...set].sort((a, b) => a - b)

	let i = 0
	let n = ranks.length
	// This only work because we know that player array is in ascending order
	for (const score of player) {
		while (i < n && score >= ranks[i]) {
			i++
		}

		res.push(n - i + 1)
	}

	return res
}
// Time complexity: O(n + m log m)
