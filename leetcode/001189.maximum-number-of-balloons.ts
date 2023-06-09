function maxNumberOfBalloons(text: string): number {
	// To construct the string "balloon" we need:
	// b: 1, a: 1, l: 2, o: 2, n: 1

	let balloonsCount = 0
	const map = new Map<string, number>()

	for (const char of text) {
		map.set(char, (map.get(char) ?? 0) + 1)
	}

	while (
		(map.get("b") ?? 0) >= 1 &&
		(map.get("a") ?? 0) >= 1 &&
		(map.get("l") ?? 0) >= 2 &&
		(map.get("o") ?? 0) >= 2 &&
		(map.get("n") ?? 0) >= 1
	) {
		balloonsCount++
		map.set("b", map.get("b")! - 1)
		map.set("a", map.get("a")! - 1)
		map.set("l", map.get("l")! - 2)
		map.set("o", map.get("o")! - 2)
		map.set("n", map.get("n")! - 1)
	}

	return balloonsCount
}
// Time complexity: O(n)
// Space complexity: O(n)

// Using division at the end for better efficiency
function maxNumberOfBalloons2(text: string): number {
	// To construct the string "balloon" we need:
	// b: 1, a: 1, l: 2, o: 2, n: 1

	const map = new Map<string, number>()

	for (const char of text) {
		map.set(char, (map.get(char) ?? 0) + 1)
	}

	const count = {
		b: map.get("b") ?? 0,
		a: map.get("a") ?? 0,
		l: Math.floor((map.get("l") ?? 0) / 2),
		o: Math.floor((map.get("o") ?? 0) / 2),
		n: map.get("n") ?? 0,
	}

	return findArrMin(Object.values(count))
}
// Time complexity: O(n)
// Space complexity: O(n)

function findArrMin(nums: number[]) {
	let min = Number.MAX_SAFE_INTEGER

	for (const num of nums) {
		if (num < min) {
			min = num
		}
	}

	return min
}
