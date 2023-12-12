import { readFileSync } from "fs"

function isNumberString(s: string) {
	return /\d/.test(s)
}

function isSymbolString(s: string) {
	return !/\d|\./.test(s)
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

	const validPathNumbers: Array<number> = []

	function isValidPathNumber(rowIdx: number, leftBoundIdx: number, rightBoundIdx: number): boolean {
		// Check if there's a symbol adjacent to the number
		// Check left side
		if (
			leftBoundIdx - 1 >= 0 &&
			(isSymbolString(rows[rowIdx]![leftBoundIdx - 1]!) || // left
				(rowIdx - 1 >= 0 && isSymbolString(rows[rowIdx - 1]![leftBoundIdx - 1]!)) || // left up
				(rowIdx + 1 < rows.length && isSymbolString(rows[rowIdx + 1]![leftBoundIdx - 1]!))) // left down
		) {
			return true
		}

		// Check right side
		if (
			rightBoundIdx + 1 < rows[rowIdx]!.length &&
			(isSymbolString(rows[rowIdx]![rightBoundIdx + 1]!) || // right
				(rowIdx - 1 >= 0 && isSymbolString(rows[rowIdx - 1]![rightBoundIdx + 1]!)) || // right up
				(rowIdx + 1 < rows.length && isSymbolString(rows[rowIdx + 1]![rightBoundIdx + 1]!))) // right down
		) {
			return true
		}

		// Check up and down
		for (let i = leftBoundIdx; i <= rightBoundIdx; i++) {
			if (
				(rowIdx - 1 >= 0 && isSymbolString(rows[rowIdx - 1]![i]!)) || // up
				(rowIdx + 1 < rows.length && isSymbolString(rows[rowIdx + 1]![i]!)) // down
			) {
				return true
			}
		}

		return false
	}

	for (let i = 0; i < rows.length; i++) {
		const row = rows[i] as string
		for (let j = 0; j < rows[i]!.length; j++) {
			const char = row[j] as string
			if (isNumberString(char)) {
				// Found the leftmost part of a number, now find it's right boundary
				let rightBoundary = j
				for (let k = rightBoundary; k < row.length && isNumberString(row[k]!); k++) {
					rightBoundary = k
				}

				if (isValidPathNumber(i, j, rightBoundary)) {
					validPathNumbers.push(parseInt(row.slice(j, rightBoundary + 1)))
				}

				j = rightBoundary + 1
			}
		}
	}

	const sumOfPathNumbers = validPathNumbers.reduce((a, b) => a + b)
	return sumOfPathNumbers
}

console.log(getSolution())
