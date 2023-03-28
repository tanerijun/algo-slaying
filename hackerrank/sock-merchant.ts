function sockMerchant(n: number, ar: number[]): number {
	type ColorMap = { [color: number]: number }
	const map: ColorMap = {}

	for (let i = 0; i < n; i++) {
		const color = ar[i]
		map[color] ? map[color]++ : (map[color] = 1)
	}

	let pairCount = 0

	for (const value of Object.values(map)) {
		pairCount += Math.floor(value / 2)
	}

	return pairCount
}
