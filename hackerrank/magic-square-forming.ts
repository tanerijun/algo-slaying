function formingMagicSquare(s: number[][]): number {
	let minCost = Number.MAX_VALUE

	// We need to find all the possible magic squares,
	// then calculate the cost using each of them

	const magicSquares = getAllMagicSquares()

	for (const magicSquare of magicSquares) {
		const cost = calculateCost(s, magicSquare)
		minCost = Math.min(minCost, cost)
	}

	return minCost
}

function calculateCost(s: number[][], magicSquare: number[][]): number {
	let cost = 0

	for (let i = 0; i < s.length; i++) {
		for (let j = 0; j < s[i].length; j++) {
			cost += Math.abs(s[i][j] - magicSquare[i][j])
		}
	}

	return cost
}

function getAllMagicSquares(): number[][][] {
	// The size of the magic square is 3x3,
	// and each number is unique.
	// So, the sum of all squares is the sum of 1 to 9 which is 45,
	// and we also know that the sum of row == column == diagonal.
	// So, the sum of each row, column, and diagonal is 45 / 3 = 15.
	const magicNumber = 15

	// There are 8 ways to sum up to 15:
	// 1 + 9 + 5
	// 2 + 8 + 5
	// 3 + 7 + 5
	// 4 + 6 + 5
	// 4 + 3 + 8
	// 6 + 2 + 7
	// 6 + 1 + 8
	// 9 + 2 + 4

	// Notice how the number 5 show up 4 times in the above list.
	// That means that the number 5 is the center of the magic square.
	// The 4 times: center horizontal line, center vertical line, and 2 diagonals.

	// Notice how the number 1, 3, 7, and 9 show up 2 times in the above list.
	// That means that the number 1, 3, 7, and 9 are the edges of the magic square.
	// The 2 times: side horizontal line, and side vertical line.
	// Ex: X is available for 2 different combinations
	// - X -
	// * | *
	// * | *

	// Notice how the number 2, 4, 6, and 8 show up 3 times in the above list.
	// That means that the number 2, 4, 6, and 8 are the corners of the magic square.
	// The 3 times: side vertical line, side horizontal line, and 1 diagonal.
	// Ex: X is available for 3 different combinations
	// X - -
	// | \ *
	// | * \

	// And these are all the possible magic squares:
	const magicSquares = [
		[
			[4, 9, 2],
			[3, 5, 7],
			[8, 1, 6],
		],
		[
			[8, 3, 4],
			[1, 5, 9],
			[6, 7, 2],
		],
		[
			[6, 1, 8],
			[7, 5, 3],
			[2, 9, 4],
		],
		[
			[2, 7, 6],
			[9, 5, 1],
			[4, 3, 8],
		],
		[
			[2, 9, 4],
			[7, 5, 3],
			[6, 1, 8],
		],
		[
			[6, 7, 2],
			[1, 5, 9],
			[8, 3, 4],
		],
		[
			[8, 1, 6],
			[3, 5, 7],
			[4, 9, 2],
		],
		[
			[4, 3, 8],
			[9, 5, 1],
			[2, 7, 6],
		],
	]

	return magicSquares
}

// Time complexity: O(1)
// Even though there are 3 loops, the number of iterations is constant.

// Extra: https://www.youtube.com/watch?v=LBUJDkRNnwg (Video explanation)

// Alternative approach to get all magic squares:
// We can just find 1 magic square, then rotate it 4 times to get a total of 4 magic squares.
// Then, we can mirror the original magic square and rotate it too to get a total of 8 magic squares.
