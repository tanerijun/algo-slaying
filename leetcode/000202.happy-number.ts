function isHappy(n: number): boolean {
	const seen = new Set<number>()

	while (n !== 1 && !seen.has(n)) {
		seen.add(n)

		let sum = 0
		while (n !== 0) {
			sum += Math.pow(n % 10, 2)
			n = Math.floor(n / 10)
		}

		n = sum
	}

	return n === 1
}
