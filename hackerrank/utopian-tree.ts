function utopianTree(n: number): number {
	let nextGrowMethod: "plus_one" | "times_2" = "times_2"
	let height = 1 // initial height

	for (let i = 0; i < n; i++) {
		if (nextGrowMethod === "plus_one") {
			height += 1
			nextGrowMethod = "times_2"
		} else {
			height *= 2
			nextGrowMethod = "plus_one"
		}
	}

	return height
}
