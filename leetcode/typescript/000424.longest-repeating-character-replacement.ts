function characterReplacement(s: string, k: number): number {
	const countMap = new Map<string, number>()
	let maxLength = 0
	let l = 0
	for (let r = 0; r < s.length; r++) {
		countMap.set(s[r], (countMap.get(s[r]) ?? 0) + 1)

		while (r - l + 1 - Math.max(...countMap.values()) > k) {
			countMap.set(s[l], countMap.get(s[l])! - 1)
			l++
		}

		maxLength = Math.max(maxLength, r - l + 1)
	}

	return maxLength
}
// Time complexity: O(n)
// Space complexity: O(26) => O(1)

// Slightly optimized solution by not scanning the whole countMap, which is O(26)
function characterReplacement2(s: string, k: number): number {
	const countMap = new Map<string, number>()
	let maxLength = 0
	let maxFrequency = 0
	let l = 0
	for (let r = 0; r < s.length; r++) {
		countMap.set(s[r], (countMap.get(s[r]) ?? 0) + 1)
		maxFrequency = Math.max(maxFrequency, countMap.get(s[r])!)

		while (r - l + 1 - maxFrequency > k) {
			// Notice how we don't need to change maxFrequency here
			// Because only larger maxFrequency will affect our final result
			// So we can ignore calculation result from the smaller maxFrequency
			// Hacky!
			countMap.set(s[l], countMap.get(s[l])! - 1)
			l++
		}

		maxLength = Math.max(maxLength, r - l + 1)
	}

	return maxLength
}
// Time complexity: O(n)
// Space complexity: O(26) => O(1)
