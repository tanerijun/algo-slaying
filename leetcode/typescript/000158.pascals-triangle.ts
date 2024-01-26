function generate(numRows: number): number[][] {
	const triangle: number[][] = []

	for (let i = 0; i < numRows; i++) {
		const row: number[] = []

		for (let j = 0; j <= i; j++) {
			if (j === 0 || j === i) {
				row.push(1)
				continue
			}

			row.push(triangle[i - 1][j - 1] + triangle[i - 1][j])
		}

		triangle.push(row)
	}

	return triangle
}
// Time complexity: O(n2)
// Space complexity: O(1) - if we don't count the output array
