function viralAdvertising(n: number): number {
	let shared = 5
	let cumulative = 0

	for (let i = 0; i < n; i++) {
		const liked = Math.floor(shared / 2)
		cumulative += liked
		shared = liked * 3
	}

	return cumulative
}
// Time complexity: O(n)
