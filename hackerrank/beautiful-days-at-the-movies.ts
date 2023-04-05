function beautifulDays(i: number, j: number, k: number): number {
	let beautifulDaysCount = 0

	for (let day = i; day <= j; day++) {
		// Difference between the number and it's reversed form
		const diff = Math.abs(day - reverse(day))
		if (diff % k === 0) {
			beautifulDaysCount++
		}
	}

	return beautifulDaysCount
}

function reverse(n: number): number {
	let res = 0

	while (n > 0) {
		res = res * 10 + (n % 10)
		n = Math.floor(n / 10)
	}

	return res
}

// Time complexity: O(|j - i|)
