function maxProfit(prices: number[]): number {
	let currMin = Number.MAX_VALUE
	let maxProfit = 0

	for (const price of prices) {
		maxProfit = Math.max(maxProfit, price - currMin)
		currMin = Math.min(currMin, price)
	}

	return maxProfit
}

// Time complexity: O(n)
// Space complexity: O(1)
