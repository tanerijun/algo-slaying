function migratoryBirds(arr: number[]): number {
	const countArr: number[] = Array(6).fill(0) // count of bird type 0 to 5
	let currentWinner: { count: number; type: number } = { count: 0, type: 0 }

	for (let i = 0; i < arr.length; i++) {
		const currentType = arr[i]
		countArr[arr[i]]++
		const currentTypeCount = countArr[arr[i]]

		if (
			currentTypeCount === currentWinner.count &&
			currentType < currentWinner.type
		) {
			currentWinner.type = currentType
		}

		if (currentTypeCount > currentWinner.count) {
			currentWinner.count = currentTypeCount
			currentWinner.type = currentType
		}
	}

	return currentWinner.type
}
// Time complexity: O(n)
