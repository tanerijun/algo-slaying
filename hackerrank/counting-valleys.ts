function countingValleys(steps: number, path: string): number {
	let valleyCount = 0
	let currentLevel = 0

	for (let i = 0; i < path.length; i++) {
		if (path[i] === "D") {
			// Every time we go down below sea level when we're not below sea level,
			// we're entering a valley
			if (currentLevel === 0) {
				valleyCount++
			}
			currentLevel--
		} else if (path[i] === "U") {
			currentLevel++
		}
	}

	return valleyCount
}
