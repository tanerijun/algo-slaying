function maximumWealth(accounts: number[][]): number {
	// Basically just find the highest value from the sum of each inner array
	let max = 0

	for (let i = 0; i < accounts.length; i++) {
		max = Math.max(
			max,
			accounts[i].reduce((a, b) => a + b)
		)
	}

	return max
}
// Time complexity: O(n2)
