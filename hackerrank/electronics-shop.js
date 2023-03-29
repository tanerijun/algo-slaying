function getMoneySpent(keyboards, drives, b) {
	const prices = []

	for (let i = 0; i < keyboards.length; i++) {
		for (let j = 0; j < drives.length; j++) {
			prices.push(keyboards[i] + drives[j])
		}
	}

	let max = -1
	for (let i = 0; i < prices.length; i++) {
		if (prices[i] <= b && prices[i] > max) {
			max = prices[i]
		}
	}

	return max
}
