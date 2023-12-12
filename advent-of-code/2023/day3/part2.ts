import { readFileSync } from "fs"

function isNumberString(s: string) {
	return /\d/.test(s)
}

function getStringContentFromFile(fPath: string): string {
	return readFileSync(fPath, "utf-8")
}

function getSolution() {
	const fPath = process.argv[2]
	if (!fPath) {
		console.error("Please provide path to input file when executing script")
		process.exit(1)
	}

	const fContent = getStringContentFromFile(fPath)
	const rows = fContent.split("\n")

	function expandNumberString(rowIdx: number, numIdx: number): string {
		const row = rows[rowIdx] as string
		let leftBound = numIdx
		let rightBound = numIdx

		// Expand left
		while (leftBound >= 0 && isNumberString(row[leftBound]!)) {
			leftBound--
		}

		// Expand right
		while (rightBound < row.length && isNumberString(row[rightBound]!)) {
			rightBound++
		}

		return row.slice(leftBound + 1, rightBound)
	}

	const gearRatios: Array<number> = []

	for (let i = 0; i < rows.length; i++) {
		for (let j = 0; j < rows[i]!.length; j++) {
			if (rows[i]![j]! === "*") {
				// Found potential gear, check for it's validity
				const adjacentPartNumbers: Array<number> = []

				// Up
				if (i - 1 >= 0) {
					const solutionSet = new Set<number>()

					// N
					if (isNumberString(rows[i - 1]![j]!)) {
						solutionSet.add(parseInt(expandNumberString(i - 1, j)))
					}
					// NE
					if (j + 1 < rows[i]!.length && isNumberString(rows[i - 1]![j + 1]!)) {
						solutionSet.add(parseInt(expandNumberString(i - 1, j + 1)))
					}
					// NW
					if (j - 1 >= 0 && isNumberString(rows[i - 1]![j - 1]!)) {
						solutionSet.add(parseInt(expandNumberString(i - 1, j - 1)))
					}

					adjacentPartNumbers.push(...solutionSet)
				}

				// Down
				if (i + 1 < rows.length) {
					const solutionSet = new Set<number>()

					// S
					if (isNumberString(rows[i + 1]![j]!)) {
						solutionSet.add(parseInt(expandNumberString(i + 1, j)))
					}
					// SE
					if (j + 1 < rows[i]!.length && isNumberString(rows[i + 1]![j + 1]!)) {
						solutionSet.add(parseInt(expandNumberString(i + 1, j + 1)))
					}
					// SW
					if (j - 1 >= 0 && isNumberString(rows[i + 1]![j - 1]!)) {
						solutionSet.add(parseInt(expandNumberString(i + 1, j - 1)))
					}

					adjacentPartNumbers.push(...solutionSet)
				}

				// E
				if (j + 1 < rows[i]!.length && isNumberString(rows[i]![j + 1]!)) {
					adjacentPartNumbers.push(parseInt(expandNumberString(i, j + 1)))
				}

				// W
				if (j - 1 >= 0 && isNumberString(rows[i]![j - 1]!)) {
					adjacentPartNumbers.push(parseInt(expandNumberString(i, j - 1)))
				}

				if (adjacentPartNumbers.length > 2) {
					throw new Error("Shouldn't happen. Try reading problem statement again!")
				}

				if (adjacentPartNumbers.length === 2) {
					let ratio = 1
					for (const partNumber of adjacentPartNumbers.values()) {
						ratio *= partNumber
					}

					gearRatios.push(ratio)
				}
			}
		}
	}

	const sumOfGearRatios = gearRatios.reduce((a, b) => a + b)
	return sumOfGearRatios
}

console.log(getSolution())
